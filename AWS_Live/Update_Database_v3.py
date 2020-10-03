from main_app_v2 import forecast_cases
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

from bs4 import BeautifulSoup as bs
from datetime import date
from selenium import webdriver

def update(region_dict, driver):
    
    df = pd.read_html(driver.page_source)[0]
    
    df.columns = ["slno", "Region", "Active_Cases", "Active_New", "Cured/Discharged", "Cured_New", "Death", "Deaths_New"]
    df["Date"] = [date.today().strftime("%d-%m-%Y") for i in range(len(df))]
    df.drop(columns=["slno", "Active_New", "Cured_New", "Deaths_New"], inplace=True)
    df = df.iloc[:-4,:]
    df.iloc[-1,0] = "India"
    df["Confirmed_Cases"] = [df.iloc[i,1:-1].astype(int).sum() for i in range(len(df))]
    cols = list(df.columns)
    cols = [i.replace(" ","_") for i in cols]
    df.columns = cols
    #df["Date"] = [date.today().strftime('%Y-%m-%d') for i in range(len(df))]
    #df.index = pd.to_datetime(df.Date,format='%Y-%m-%d')
    df["Date"] = [date.today().strftime('%d-%m-%Y') for i in range(len(df))]
    df.index = pd.to_datetime(df.Date,format='%d-%m-%Y')
    for i,region in enumerate(region_dict):
        region_dict[region] = region_dict[region].append(df[df.Region == region], sort=False, ignore_index=True)
        try:
            region_dict[region].index = pd.to_datetime(region_dict[region].Date,format='%d-%m-%Y')
        except:
            region_dict[region].index = pd.to_datetime(region_dict[region].Date,format='%Y-%m-%d')
        
    return region_dict

def update_database():
    
    df = pd.read_csv("COVID_Database.csv")
    cols = list(df.columns)
    cols = [i.replace(" ","_") for i in cols]
    df.columns = cols

    states_df = df.groupby('Region')
    state_df = [pd.DataFrame(states_df.get_group(state)) for state in states_df.groups]
    
    #selenium setup
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver",chrome_options=options)
    driver.get("https://www.mohfw.gov.in/")
    
    region_dict = {}
    for region in states_df.groups:
        region_dict[region] = pd.DataFrame(states_df.get_group(region))
        try:
            region_dict[region].index = pd.to_datetime(region_dict[region].Date,format='%Y-%m-%d')
        except:
            region_dict[region].index = pd.to_datetime(region_dict[region].Date,format='%d-%m-%Y')

        region_dict = update(region_dict, driver)
    #     break
    
    driver.quit()
    
    df = pd.DataFrame()
    for region in region_dict.keys():
        df = df.append(region_dict[region], sort=False, ignore_index=True)

    cols = list(df.columns)
    cols = [i.replace(" ","_") for i in cols]
    df.columns = cols
    df.drop_duplicates(inplace=True)
    
    df.to_csv("COVID_Database.csv", index=False)
    
    return "Database Updated"


def forecasted_database():    
    df = pd.read_csv("COVID_Database.csv")
    df["Forecasted"] = ["" for i in range(len(df))]
    regions = sorted(list(df.Region.value_counts().keys()))

    df_old = pd.read_csv("Forecast.csv")
    
    forecast_df = pd.DataFrame(columns=['Date', 'Region', 'Confirmed_Cases', 'Active_Cases', 'Cured/Discharged',
           'Death', 'Forecasted', 'Forecasted_high', 'Forecasted_low', 'Confirmed_Cases_Daywise'])
    
    forecasts = []
    forecasts_high = []
    forecasts_low = []
    forecasts_daywise = []
    forecasts_daywise_high = []
    forecasts_daywise_low = []
    days = []
    region_x = []
#     forecasted = []
#     forecasted_region = []
    n=31
    for region in regions:
        try:
            forecast,std_error,confidence_interval = forecast_cases(region, n=n, return_all=True)
            
            try:
                forecast_old = df_old.Forecasted_Cases[df_old.Region==region].iloc[0]
                forecast_old = forecast[0]-forecast_old
                forecasts_daywise.append(forecast_old)
                forecasts_daywise_high.append(forecast_old+(forecast_old*0.05))
                forecasts_daywise_low.append(forecast_old-(forecast_old*0.05))

            except:
                pass
                
            forecast_high = confidence_interval[:,1]
            forecast_low = confidence_interval[:,0]
            forecasts.extend(forecast)
            forecasts_high.extend(forecast_high)
            forecasts_low.extend(forecast_low)
            forecasts_daywise.extend(pd.Series(forecast).diff(periods=1).iloc[1:])
            forecasts_daywise_high.extend(pd.Series(forecast_high).diff(periods=1).iloc[1:])
            forecasts_daywise_low.extend(pd.Series(forecast_low).diff(periods=1).iloc[1:])
            days.extend(pd.date_range(date.today(), periods=n).strftime('%d-%m-%Y'))
            region_x.extend([region for i in range(n)])
    #         forecasted.append(forecast[0])
    #         forecasted_region.append(region)
        except:
            pass

    forecast_df.Forecasted = forecasts
    forecast_df.Date = days
    forecast_df.Region = region_x
    forecast_df.Forecasted_high = forecasts_high
    forecast_df.Forecasted_low = forecasts_low
    forecast_df["Forecasted_Cases_Daywise"] = forecasts_daywise
    forecast_df["Forecasted_Cases_high_Daywise"] = forecasts_daywise_high
    forecast_df["Forecasted_Cases_low_Daywise"] = forecasts_daywise_low
    forecast_df.index = pd.to_datetime(forecast_df.Date)

    df2 = pd.concat([df,forecast_df], join='outer', ignore_index=True)
    df2 = df2.groupby("Region", as_index=False).apply(lambda x: x.iloc[:-1])
    df2.index = df2.Date 
    
    
    cols = ['Confirmed_Cases', 'Active_Cases', 'Cured/Discharged', 'Death']
    for col in cols:
        df2[col] = df2[col].shift(-1)
    df2 = df2.dropna(how="all",subset=['Confirmed_Cases', 'Active_Cases','Forecasted'])

    for region in regions:
        df2.Confirmed_Cases_Daywise[df2.Region==region] = df2.Confirmed_Cases[df2.Region==region].diff(periods=1)

    df2.to_csv("COVID_Forecasted.csv", index=False)

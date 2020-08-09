
import pandas as pd
import numpy as np
# from statsmodels.tsa.arima_model import ARIMA
# import matplotlib.pyplot as plt
# import itertools
import warnings
warnings.filterwarnings("ignore")

import requests
from bs4 import BeautifulSoup as bs
from datetime import date

def update(region_dict):
    res = requests.get("https://prsindia.org/covid-19/cases")
    soup = bs(res.content,'lxml')
    table = soup.find_all('table')[0] 
    df = pd.read_html(str(table))[0]
    df.drop(columns=["#"], inplace=True)
    cols = list(df.columns)
    cols[0] = "Region"
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

    region_dict = {}
    for region in states_df.groups:
        region_dict[region] = pd.DataFrame(states_df.get_group(region))
        try:
            region_dict[region].index = pd.to_datetime(region_dict[region].Date,format='%Y-%m-%d')
        except:
            region_dict[region].index = pd.to_datetime(region_dict[region].Date,format='%d-%m-%Y')

        region_dict = update(region_dict)
    #     break

    df = pd.DataFrame()
    for region in region_dict.keys():
        df = df.append(region_dict[region], sort=False, ignore_index=True)

    cols = list(df.columns)
    cols = [i.replace(" ","_") for i in cols]
    df.columns = cols
    df.drop_duplicates(inplace=True)
    
    df.to_csv("COVID_Database.csv", index=False)
    
    return "Database Updated"

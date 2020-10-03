
import pandas as pd
import numpy as np
from statsmodels.tsa.arima_model import ARIMA
import matplotlib.pyplot as plt
import itertools
import warnings
warnings.filterwarnings("ignore")

import requests
from bs4 import BeautifulSoup as bs
from datetime import date, timedelta
from datetime import datetime as d
import joblib


def keep_in_memory():
    today = date.today().strftime('%d-%m-%Y')
    yesterday = (date.today()-timedelta(days=1)).strftime('%d-%m-%Y')
    #day_bfr_yesterday = (date.today()-timedelta(days=2)).strftime('%d-%m-%Y')
    df = pd.read_csv("Forecast.csv")
    if d.strptime(df.Date.iloc[0], '%d-%m-%Y') > d.strptime(yesterday, '%d-%m-%Y'):
        return False
    df = pd.read_csv("COVID_Forecasted.csv")
    df = df[df.Date==yesterday]
    regions = list(df.Region)
    forecasted = list(df.Forecasted)
    forecasted_active = list(df.Forecasted_active)
    df = pd.DataFrame(columns=["Date", "Region", "Forecasted_Cases", "Forecasted_Active_Cases"])
    df.Region = regions
    df.Forecasted_Cases = forecasted
    df.Forecasted_Cases.bfill(inplace=True)
    
    ##### Active Cases #####
    df.Forecasted_Active_Cases = forecasted_active
    df.Forecasted_Active_Cases.bfill(inplace=True)
    
    df.drop_duplicates(inplace=True)
    df.Date = [today for i in range(len(df))]
    df.to_csv("Forecast.csv", index=False)
    return True

def get_previous_cases(region):
    df = pd.read_csv("COVID_Database.csv")
    df.index = df.Date
    try:
        yesterday = df.Confirmed_Cases[df.Region==region][str(date.today().strftime('%d-%m-%Y'))]
        as_on = str(date.today())
    except:
        yesterday = df.Confirmed_Cases[df.Region==region][-1]
        as_on = df.Date[df.Region==region][-1]
    
    del df
    return yesterday, as_on

def find_best_params(state, pdq):
    aic_values = []
    for param in pdq:
        try:
            #initilizing ARIMA model
            model = ARIMA(state, order=param)
            model_fit = model.fit()
#             print(param, model_fit.aic)
            aic_values.append([param, model_fit.aic])
        except:
            pass

    aic_values = np.array(aic_values)
    a = np.where(aic_values == aic_values[:,1].min())[0][0]
    return aic_values[a][0]

def fit_model(force_train=False):

    run_rest = keep_in_memory()
    
    if force_train:
        run_rest = True
        
    if not run_rest:
        return "Please Update Database"
    
    df = pd.read_csv("COVID_Database.csv")
    cols = list(df.columns)
    cols = [i.replace(" ","_") for i in cols]
    df.columns = cols

    states_df = df.groupby('Region')
    state_df = [pd.DataFrame(states_df.get_group(state)) for state in states_df.groups]
    
    p=range(0,9)
    d=range(0,3)
    q=range(0,5)
    pdq = list(itertools.product(p,d,q))

    state_model = {}
    for state in state_df[:]:
        
        try:
            state.index = pd.to_datetime(state.Date,format='%Y-%m-%d')
        except:
            state.index = pd.to_datetime(state.Date,format='%d-%m-%Y')
    #     state.drop(columns=["Date","Region"], axis=1, inplace=True)

        print("Processing:", state.Region[0])

        #state.Confirmed_Cases_diff = state.Confirmed_Cases
        params = find_best_params(state.Confirmed_Cases, pdq)

        #initilizing ARIMA model
        model = ARIMA(state.Confirmed_Cases, order=params)
        model_fit = model.fit()
#         print(params)

        state_model[str(state.Region[0])] = model_fit

#         break

    for region in state_model.keys():
        joblib.dump(state_model[region], region+".ml")
        
#     print("DONE")
    return "DONE"

def forecast_cases(region, n=7, return_all=False):
    
    model_fit = joblib.load(region+".ml")
    # multi-step out-of-sample forecast
    forecast, std_error, confidence_interval = model_fit.forecast(steps=n)
    forecast = [round(cases) for cases in forecast]
    if return_all:
        return forecast, std_error, confidence_interval
    else:
        return forecast



###################### Active Cases ######################

def fit_model_active_cases(force_train=False):

#     run_rest = keep_in_memory()
    run_rest = True
    
    if force_train:
        run_rest = True
        
    if not run_rest:
        return "Please Update Database"
    
    df = pd.read_csv("COVID_Database.csv")
    cols = list(df.columns)
    cols = [i.replace(" ","_") for i in cols]
    df.columns = cols

    states_df = df.groupby('Region')
    state_df = [pd.DataFrame(states_df.get_group(state)) for state in states_df.groups]
    
    p=range(0,9)
    d=range(0,3)
    q=range(0,5)
    pdq = list(itertools.product(p,d,q))

    state_model = {}
    for state in state_df[:]:
        
        try:
            state.index = pd.to_datetime(state.Date,format='%Y-%m-%d')
        except:
            state.index = pd.to_datetime(state.Date,format='%d-%m-%Y')
    #     state.drop(columns=["Date","Region"], axis=1, inplace=True)

        print("Processing:", state.Region[0])

        #state.Confirmed_Cases_diff = state.Confirmed_Cases
        params = find_best_params(state.Active_Cases, pdq)

        #initilizing ARIMA model
        model = ARIMA(state.Active_Cases, order=params)
        model_fit = model.fit()
#         print(params)

        state_model[str(state.Region[0])] = model_fit

#         break

    for region in state_model.keys():
        joblib.dump(state_model[region], region+"_active.ml")
        
#     print("DONE")
    return "DONE"


def forecast_cases_active(region, n=7, return_all=False):
    
    model_fit = joblib.load(region+"_active.ml")
    # multi-step out-of-sample forecast
    forecast, std_error, confidence_interval = model_fit.forecast(steps=n)
    forecast = [round(cases) for cases in forecast]
    if return_all:
        return forecast, std_error, confidence_interval
    else:
        return forecast
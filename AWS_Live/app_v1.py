from main_app_v1 import fit_model, forecast_cases, get_previous_cases
from Update_Database import update_database
from datetime import date, timedelta
from datetime import datetime as d
from pandas import date_range
import pandas as pd
import plotly.graph_objects as go
import flask
from flask import request
app = flask.Flask(__name__)
app.config["DEBUG"] = True
from flask_cors import CORS

def embbed_graph(region):
    df = pd.read_csv(r"C:\Users\Tejas\Downloads\COVID-19 Cases(12-07-2020).csv")
    df.drop(columns=["S. No."],inplace=True)
    states_df = df.groupby('Region')
    #Create the graph
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=pd.DataFrame(states_df.get_group(region))["Date"], y=pd.DataFrame(states_df.get_group(region))["Confirmed_Cases"], mode='lines+markers', name='Confirmed Cases'))
    fig.add_trace(go.Scatter(x=pd.DataFrame(states_df.get_group(region))["Date"], y=pd.DataFrame(states_df.get_group(region))["Active_Cases"], mode='lines+markers', name='Active Cases'))
    fig.add_trace(go.Scatter(x=pd.DataFrame(states_df.get_group(region))["Date"], y=pd.DataFrame(states_df.get_group(region))["Cured/Discharged"], mode='lines+markers', name='Cured/Discharged'))
    fig.add_trace(go.Scatter(x=pd.DataFrame(states_df.get_group(region))["Date"], y=pd.DataFrame(states_df.get_group(region))["Death"], mode='lines+markers', name='Deaths'))

    #fig.update_xaxes(tickangle=45, tickformat = '%d-%m')
    
    #Edit the layout
    fig.update_layout(template='plotly_white', legend=dict(x=0.01, y=0.99), margin=dict(l=20, r=20, t=50, b=20))
    fig.update_layout(title='COVID-19 Cases', xaxis_title='Date', yaxis_title='Number of Cases')
    # fig.show()
    
    go_fig = fig.to_html(full_html=False)
    
    return go_fig

def result_to_html(result, region):
    today, yesterday, as_on = get_previous_cases(region)
    as_on = d.strptime(date.today().strftime('%Y-%m-%d'), "%Y-%m-%d").date()
    res='<h1 style="text-align:center;"> COVID-19 Forecasts For {} </h1>\n'.format(region)
    res+='<div class="container" style="display: flex; height: 600px;">\n'
    res+='<div style="width: 20%; padding: 50px 10px 10px 10px;" class="temp_1">'
    res+='<table>\n'
    yesterday_d = (as_on-timedelta(days=1)).strftime('%Y-%m-%d')
    dates = date_range(yesterday_d, periods=7).strftime('%Y-%m-%d')
    result = zip(dates,result)
    res+='<thead>\n'
    res+='<style> table, th, td {border: 2px solid black; border-collapse: collapse;} </style>'
    res+='<tr><th style="width: 40%; padding: 10px 10px 10px 10px;"><h3> Date </h3></th><th style="padding: 10px 10px 10px 10px;"><h3>Predicted No. of Cases</h3></th></tr>\n'
    #res+='</thead>\n'
    res+='<tbody>'
    res+='<style> table, th, td {border: 2px solid black; border-collapse: collapse;} </style>' #padding-left:20px; padding-right:20px;} </style>'
    for row in result:
        res+='<tr><td style="padding-left:0px; padding-right:0px;"><h3>&nbsp;&nbsp;&nbsp;&nbsp;{} </h3></td> <td style="padding-left:10px; padding-right:10px;"><h3>{} &#177; &nbsp; 5%</h3></td></tr>\n'.format(row[0],row[1])
    res+='</tbody>'
    res+='</table>\n\n'
    res+='<h4>Confirmed Cases as of Yesterday : {}</h4>\n'.format(yesterday)
    res+='<h4>Confirmed Cases as of Today : {}</h4>\n'.format(today)
    res+='<h4>As on : {}</h4>\n'.format(as_on)
    res+='<h4>Data Source Used for Training: <br> <a href="https://prsindia.org/covid-19/cases"> Visit prsindia.org</a></h4>'
    res+='</div>\n'
    res+='<div style="flex-grow: 1; padding: 10px 10px 10px 10px;" class="temp_2">\n'
    res+=embbed_graph(region)
    res+='</div>\n'
    res+='</div>\n'
    return res

CORS(app)

# main index page route
@app.route('/')
def home():
    return '<h1>API is working.. </h1>'


@app.route('/forecast',methods=['GET'])
def forecast():
    region = str(request.args["region"])
    forecast = forecast_cases(region)
    
    return result_to_html(forecast, region)

@app.route('/update')
def update():
    update_database()
    
    return "Database Updated"

@app.route('/train')
def train():
    fit_model()
    
    return "Database Updated"


if __name__ == "__main__":
    app.run(debug=True)

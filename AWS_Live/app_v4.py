from main_app_v3 import fit_model, forecast_cases, get_previous_cases
from Update_Database_v4 import update_database
from website_elements_v4 import get_menu, get_menu_mobile, get_about, get_about_mobile, get_news, get_news_mobile, embbed_graph, embbed_graph_mobile, add_cases_compare, add_cases_compare_mobile
from datetime import date, timedelta
from datetime import datetime as d
from pandas import date_range
import re
# import pandas as pd
# import plotly.graph_objects as go
import flask
from flask import request, redirect, url_for
app = flask.Flask(__name__)
app.config["DEBUG"] = True
from flask_cors import CORS

visitors_count = 228
visitors_count_desktop = 0
visitors_count_mobile = 0
visitors_count_other = 0

def result_to_html(result, region):
    yesterday, as_on = get_previous_cases(region)
    as_on = d.strptime(date.today().strftime('%Y-%m-%d'), "%Y-%m-%d").date()
    res=get_menu()
    res+='<div style="width: 100%; padding: 30px 0px 0px 0px; text-align: left;">\n'
    res+='<div class="container" style="display: flex; height: 600px;">\n'
    res+='<div style="width: 20%; padding: 0px 0px 10px 10px;" class="temp_1">\n'
    res+='<h5 style="font-size: 14px;"><strong style="font-size: 20px;"> In {} </strong> <br> as on : {}</h5>\n'.format(region, as_on)
    res+='<table id="t01" style="height: 40px;">\n'
    yesterday_d = (as_on-timedelta(days=1)).strftime('%Y-%m-%d')
    dates = date_range(as_on, periods=7).strftime('%Y-%m-%d')
    result = zip(dates,result)
    res+='<thead>\n'
    res+='<style> table, th, td {border: 2px solid black; border-collapse: collapse; height: 40px;} </style>'
    res+='<tr><th style="width: 40%; padding: 10px 10px 10px 10px;"><h3 style="text-align: center;"> Date </h3></th><th style="padding: 10px 10px 10px 10px;"><h3 style="text-align: center;">Predicted No. of Cases &#177;&nbsp; 5%</h3></th></tr>\n'
    res+='<tbody>'
    res+='<style> table, th, td {border: 2px solid black; border-collapse: collapse;} </style>' #padding-left:20px; padding-right:20px;} </style>'
    for row in result:
        res+='<tr><td style="padding-left:0px; padding-right:0px;"><h3 style="text-align: center;">&nbsp; {} &nbsp;</h3></td> <td style="padding-left:10px; padding-right:10px;"><h3 style="text-align: center;"> {} </h3></td></tr>\n'.format(row[0],row[1])
    res+='</tbody>'
    res+='</table>\n\n'
    res+='<p style="font-size: 14px; line-height: 1.6;"><strong>Confirmed Cases for Yesterday : {}</strong><br>'.format((yesterday))
#     res+='<strong>Confirmed Cases as of Today : {}</strong><br>\n'.format(today)
    res+='<strong>Daily Update Time: 05:00 UTC</strong></p>'
    res+='<p style="font-size: 14px; line-height: 1.6;"><strong><a href="http://covidforecasts.xyz/About">Click here to know more about our source</a></strong></p>'
    res+='</div>\n'
    res+='<div style="flex-grow: 1; padding: 10px 10px 10px 10px;" class="temp_2">\n'
    res+=embbed_graph(region)
    res+=add_cases_compare(region, as_on, yesterday)
    res+='</div>\n'
    res+='</div>\n'
    res+='<footer style="padding: 12px 0px 0px 0px;" margin: 0;> <a href="http://covidforecasts.xyz/About">About</a> &emsp; | &emsp; <a href="http://covidforecasts.xyz/About#section2">Contact Us</a> </footer>'
    return res

def result_to_html_mobile(result, region):
    yesterday, as_on = get_previous_cases(region)
    as_on = d.strptime(date.today().strftime('%Y-%m-%d'), "%Y-%m-%d").date()
    res=get_menu_mobile()
    res+='<div style="width: 100%; padding: 20px 0px 0px 0px;">\n'
#     res+='<div class="container" style="display: flex; height: 600px;">\n'
#     res+='<div style="width: 100%; padding: 10px 10px 10px 10px;" class="temp_1">\n'
    res+='<h5 style="font-size: 14px; padding: 0px 0px 0px 20px;"><strong style="font-size: 20px;"> In {} </strong> <br> as on : {}</h5>\n '.format(region, as_on)
    res+='<div style="flex-grow: 1; padding: 0px 10px 10px 10px; width:95%; height: 400px;" class="temp_2">\n'
    res+=embbed_graph_mobile(region)
    res+='<p style="margin: auto;"> &nbsp; &emsp; Note: Graph is best viewed on desktop &emsp; </p>\n'
    res+='</div>\n'
    res+='<div style="width: 80%; padding: 30px 0px 50px 0px; margin-left:auto; margin-right:auto;">\n'
    res+='<table id="t01" style="margin-left:auto; margin-right:auto; height: 40px;">\n'
    yesterday_d = (as_on-timedelta(days=1)).strftime('%Y-%m-%d')
    dates = date_range(as_on, periods=7).strftime('%Y-%m-%d')
    result = zip(dates,result)
    res+='<thead>\n'
    res+='<style> table, th, td {border: 2px solid black; border-collapse: collapse;} </style>'
    res+='<tr><th style="width: 40%; padding: 10px 10px 10px 10px;"><h3 style="text-align: center;"> Date </h3></th><th style="padding: 10px 10px 10px 10px;"><h3 style="text-align: center;">Predicted No. of Cases &#177;&nbsp; 5%</h3></th></tr>\n'
    res+='<tbody>'
    res+='<style> table, th, td {border: 2px solid black; border-collapse: collapse; height: 40px;} </style>' #padding-left:20px; padding-right:20px;} </style>'
    for row in result:
        res+='<tr><td style="padding-left:0px; padding-right:0px; padding: 0px 0px 0px 0px;"><h3 style="text-align: center;">&nbsp; {} &nbsp;</h3></td> <td style="padding-left:10px; padding-right:10px;"><h3 style="text-align: center;"> {} </h3></td></tr>\n'.format(row[0],row[1])
    res+='</tbody>'
    res+='</table>\n\n'
    res+='<p style="font-size: 14px; line-height: 1.8;"><strong>Confirmed Cases for Yesterday : {}</strong><br>'.format((yesterday))
    res+='<strong>Daily Update Time: 05:00 UTC</strong></p>'
    res+='<p style="font-size: 14px; line-height: 1.6;"><strong><a href="http://covidforecasts.xyz/About">Click here to know more about our source</a></strong></p>'
    #
    res+=add_cases_compare_mobile(region, as_on, yesterday)
    res+='</div>\n'
    res+='</div>\n'
    res+='<footer style="padding: 12px 0px 0px 0px;" margin: 0;> <a href="http://covidforecasts.xyz/About">About</a> &emsp; | &emsp; <a href="http://covidforecasts.xyz/About#section2">Contact Us</a> </footer>\n'
    return res

def result_to_html_other(result, region):
    yesterday, as_on = get_previous_cases(region)
    as_on = d.strptime(date.today().strftime('%Y-%m-%d'), "%Y-%m-%d").date()
    res=get_menu()
    res+='<div style="width: 100%; padding: 30px 0px 0px 0px;">\n'
    res+='<div class="container" style="display: flex; height: 600px;">\n'
    res+='<div style="width: 20%; padding: 0px 0px 10px 10px;" class="temp_1">\n'
    res+='<h5 style="font-size: 14px;"><strong style="font-size: 20px;"> In {} </strong> <br> as on : {}</h5>\n'.format(region, as_on)
    res+='<table id="t01" style="height: 40px;">\n'
    yesterday_d = (as_on-timedelta(days=1)).strftime('%Y-%m-%d')
    dates = date_range(as_on, periods=7).strftime('%Y-%m-%d')
    result = zip(dates,result)
    res+='<thead>\n'
    res+='<style> table, th, td {border: 2px solid black; border-collapse: collapse; height: 40px;} </style>'
    res+='<tr><th style="width: 40%; padding: 10px 10px 10px 10px;"><h3 style="text-align: center;"> Date </h3></th><th style="padding: 10px 10px 10px 10px;"><h3 style="text-align: center;">Predicted No. of Cases &#177;&nbsp; 5%</h3></th></tr>\n'
    res+='<tbody>'
    res+='<style> table, th, td {border: 2px solid black; border-collapse: collapse;} </style>' #padding-left:20px; padding-right:20px;} </style>'
    for row in result:
        res+='<tr><td style="padding-left:0px; padding-right:0px;"><h3 style="text-align: center;">&nbsp; {} &nbsp;</h3></td> <td style="padding-left:10px; padding-right:10px;"><h3 style="text-align: center;"> {} </h3></td></tr>\n'.format(row[0],row[1])
    res+='</tbody>'
    res+='</table>\n\n'
    res+='<p style="font-size: 14px; line-height: 1.6;"><strong>Confirmed Cases for Yesterday : {}</strong><br>'.format((yesterday))
#     res+='<strong>Confirmed Cases as of Today : {}</strong><br>\n'.format(today)
    res+='<strong>Daily Update Time: 05:00 UTC</strong></p>'
    res+='<p style="font-size: 14px; line-height: 1.6;"><strong><a href="http://covidforecasts.xyz/About">Click here to know more about our source</a></strong></p>'
    res+='</div>\n'
    res+='<div style="flex-grow: 1; padding: 10px 10px 10px 10px;" class="temp_2">\n'
    res+=embbed_graph(region)
    res+=add_cases_compare(region, as_on, yesterday)
    res+='</div>\n'
    res+='</div>\n'
    res+='</div>\n'
    res+='<footer style="padding: 12px 0px 0px 0px; position: relative; bottom: -300px;"> <a href="http://covidforecasts.xyz/About">About</a> &emsp; | &emsp; <a href="http://covidforecasts.xyz/About#section2">Contact Us</a> </footer>\n'
    return res


CORS(app)

# main index page route
@app.route('/')
def home():
    return redirect(url_for('Home'))

@app.route('/Home')
def Home():

    req_time = d.now()
    req_time = req_time.strftime("%c")
    
    global visitors_count
    visitors_count+=1
    with open("visitors_count.txt", "a+") as file:
        file.write(str((req_time, request.remote_addr, visitors_count))+'\n')
        
    region = "India"
    forecast = forecast_cases(region)
    agent = request.headers.get('User-Agent')
    pattern = r"(Windows|CrOS|Android|Macintosh|iPhone|ipad|iPod)"
    try:
        agent = re.findall(pattern, agent)[0]
    except:
        agent = "Windows"
#     if agent in ["Windows", "Macintosh", "CrOS"]:
#         print("Desktop")
    if agent in ["Android", "iPhone", "ipad", "iPod"]:
        global visitors_count_mobile
        visitors_count_mobile+=1
        with open("visitors_count_mobile.txt", "a+") as file:
            file.write(str((req_time, request.remote_addr, visitors_count_mobile))+'\n')
            
        return result_to_html_mobile(forecast, region)
    else:
        global visitors_count_desktop
        visitors_count_desktop+=1
        with open("visitors_count_desktop.txt", "a+") as file:
            file.write(str((req_time, request.remote_addr, visitors_count_desktop))+'\n')
        
        return result_to_html(forecast, region)
        
@app.route('/About')
def About():
    agent = request.headers.get('User-Agent')
    pattern = r"(Windows|CrOS|Android|Macintosh|iPhone|ipad|iPod)"
    try:
        agent = re.findall(pattern, agent)[0]
    except:
        agent = "Windows"
#     if agent in ["Windows", "Macintosh", "CrOS"]:
#         print("Desktop")
    if agent in ["Android", "iPhone", "ipad", "iPod"]:
        return get_about_mobile()
    else:
        return get_about()
        
        
@app.route('/News')
def News():
    agent = request.headers.get('User-Agent')
    pattern = r"(Windows|CrOS|Android|Macintosh|iPhone|ipad|iPod)"
    try:
        agent = re.findall(pattern, agent)[0]
    except:
        agent = "Windows"
#     if agent in ["Windows", "Macintosh", "CrOS"]:
#         print("Desktop")
    if agent in ["Android", "iPhone", "ipad", "iPod"]:
        return get_news_mobile()
    else:
        return get_news()


@app.route('/forecast',methods=['GET'])
def forecast():
    region = str(request.args["region"])
    forecast = forecast_cases(region)
    agent = request.headers.get('User-Agent')
    pattern = r"(Windows|CrOS|Android|Macintosh|iPhone|ipad|iPod)"
    try:
        agent = re.findall(pattern, agent)[0]
    except:
        agent = "Windows"
#     if agent in ["Windows", "Macintosh", "CrOS"]:
#         print("Desktop")
    if agent in ["Android", "iPhone", "ipad", "iPod"]:
        return result_to_html_mobile(forecast, region)
    else:
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
    app.run(debug=True, port='80',host='0.0.0.0')


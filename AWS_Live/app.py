from main_app import fit_model, forecast_cases, get_previous_cases
from Update_Database import update_database
from datetime import date, timedelta
from datetime import datetime as d
from pandas import date_range
import flask
from flask import request
app = flask.Flask(__name__)
app.config["DEBUG"] = True
from flask_cors import CORS

def result_to_html(result, region):
    today, yesterday, as_on = get_previous_cases(region)
    as_on = d.strptime('2020-07-15', "%Y-%m-%d").date()
    res='<h2> COVID-19 Forecasts For {}</h2>\n'.format(region)
    res+='<table>\n'
    yesterday_d = (as_on-timedelta(days=1)).strftime('%Y-%m-%d')
    dates = date_range(yesterday_d, periods=7).strftime('%Y-%m-%d')
    result = zip(dates,result)
    res+='<thead>\n'
    res+='<tr><th><h2> Date ::</h2></th><th><h2>Predicted No. of Cases</h2></th></tr>\n'
    res+='</thead>\n'
    res+='<tbody>'
    for row in result:
        res+='<tr><td><h2>&nbsp;&nbsp;&nbsp;&nbsp;{} :</h2></td><td><h2>{} &#177; &nbsp; 5%</h2></td></tr>\n'.format(row[0],row[1])
    res+='</tbody>'
    res+='</table>\n\n'
    res+='<h3>Confirmed Cases as of Yesterday : {}</h3>\n'.format(yesterday)
    res+='<h3>Confirmed Cases as of Today : {}</h3>\n'.format(today)
    res+='<h3>As on : {}</h3>\n'.format(as_on)
    res+='<h3>Data Source Used for Training: <a href="https://prsindia.org/covid-19/cases">Visit prsindia.org</a></h3>'
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
    app.run(debug=True, port='9000',host='0.0.0.0')

import pandas as pd
import plotly.graph_objects as go

def embbed_graph(region):
    updatemenus = list([    dict(active=0, buttons=list([
            dict(label = 'Confirmed Cases-Cumilative',
                 method = 'update',
                 args = [{'visible': [True, True, True, True, True, True, True, False, False, False, False, False, False, False, False, False, False, False]},
                         {'title': 'COVID-19 Cases Forecast - Total Cases',
                          'annotations': ''}]),
            dict(label = 'Confirmed Cases-New',
                 method = 'update',
                 args = [{'visible': [False, False, False, False, False, False, False, False, False, False, True, True, True, True, False, False, False, False]},
                         {'title': 'COVID-19 Cases Forecast - New Cases',
                          'annotations': ''}]),

            dict(label = 'Active Cases-Cumilative',
                 method = 'update',
                 args = [{'visible': [True, True, True, True, False, False, False, True, True, True, False, False, False, False, False, False, False, False]},
                         {'title': 'COVID-19 Cases Forecast - Total Cases',
                          'annotations': ''}]),
            dict(label = 'Active Cases-New',
                 method = 'update',
                 args = [{'visible': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, True, True]},
                         {'title': 'COVID-19 Cases Forecast - Active Cases',
                          'annotations': ''}]),        ]),                   

            x = 0.01,
            xanchor = 'left',
            y = 1.05,
            yanchor = 'top',    ),   ])

    df = pd.read_csv("COVID_Database.csv")
    states_df = df.groupby('Region')
    df = pd.read_csv("COVID_Forecasted.csv")
    states_df2 = df.groupby('Region')
    #Create the graph
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=pd.DataFrame(states_df2.get_group(region))["Date"][:-1], y=pd.DataFrame(states_df2.get_group(region))["Confirmed_Cases"], mode='lines+markers', name='Confirmed Cases'))
    fig.add_trace(go.Scatter(x=pd.DataFrame(states_df2.get_group(region))["Date"][:-1], y=pd.DataFrame(states_df2.get_group(region))["Active_Cases"], mode='lines', name='Active Cases'))
    fig.add_trace(go.Scatter(x=pd.DataFrame(states_df2.get_group(region))["Date"][:-1], y=pd.DataFrame(states_df2.get_group(region))["Cured/Discharged"], mode='lines', name='Cured/Discharged'))
    fig.add_trace(go.Scatter(x=pd.DataFrame(states_df2.get_group(region))["Date"][:-1], y=pd.DataFrame(states_df2.get_group(region))["Death"], mode='lines', name='Deaths'))
    fig.add_trace(go.Scatter(x=pd.DataFrame(states_df2.get_group(region))["Date"][:-1], y=pd.DataFrame(states_df2.get_group(region))["Forecasted"], mode='lines+markers', name='Forecasted Cases', line=dict(color='rgb(255, 100, 50)'), legendgroup="Forecasts"))
    fig.add_trace(go.Scatter(x=pd.DataFrame(states_df2.get_group(region))["Date"][:-1], y=pd.DataFrame(states_df2.get_group(region))["Forecasted_high"], mode='lines', name='Forecasted Cases', fill=None, line=dict(color='rgb(255, 150, 50)'), legendgroup="Forecasts", showlegend=False))
    fig.add_trace(go.Scatter(x=pd.DataFrame(states_df2.get_group(region))["Date"][:-1], y=pd.DataFrame(states_df2.get_group(region))["Forecasted_low"], mode='lines', name='Forecasted Cases', line=dict(color='rgb(255, 150, 50)'), fill='tonexty', legendgroup="Forecasts", showlegend=False))

    ######################
    fig.add_trace(go.Scatter(x=pd.DataFrame(states_df2.get_group(region))["Date"][:-1], y=pd.DataFrame(states_df2.get_group(region))["Forecasted_active"], mode='lines+markers', name='Forecasted Active Cases', line=dict(color='rgb(255, 100, 50)'), legendgroup="Forecasts", visible=False))
    fig.add_trace(go.Scatter(x=pd.DataFrame(states_df2.get_group(region))["Date"][:-1], y=pd.DataFrame(states_df2.get_group(region))["Forecasted_active_high"], mode='lines', name='Forecasted Active Cases', fill=None, line=dict(color='rgb(255, 150, 50)'), legendgroup="Forecasts", showlegend=False, visible=False))
    fig.add_trace(go.Scatter(x=pd.DataFrame(states_df2.get_group(region))["Date"][:-1], y=pd.DataFrame(states_df2.get_group(region))["Forecasted_active_low"], mode='lines', name='Forecasted Active Cases', line=dict(color='rgb(255, 150, 50)'), fill='tonexty', legendgroup="Forecasts", showlegend=False, visible=False))



    fig.add_trace(go.Scatter(x=pd.DataFrame(states_df2.get_group(region))["Date"][:-1], y=pd.DataFrame(states_df2.get_group(region))["Confirmed_Cases_Daywise"], mode='lines+markers', name='Confirmed Cases', visible=False))
    fig.add_trace(go.Scatter(x=pd.DataFrame(states_df2.get_group(region))["Date"][:-1], y=pd.DataFrame(states_df2.get_group(region))["Forecasted_Cases_Daywise"], mode='lines+markers', name='Forecasted Cases', line=dict(color='rgb(255, 100, 50)'), legendgroup="Forecasts", visible=False))
    fig.add_trace(go.Scatter(x=pd.DataFrame(states_df2.get_group(region))["Date"][:-1], y=pd.DataFrame(states_df2.get_group(region))["Forecasted_Cases_high_Daywise"], mode='lines', name='Forecasted Cases', fill=None, line=dict(color='rgb(255, 150, 50)'), legendgroup="Forecasts", showlegend=False, visible=False))
    fig.add_trace(go.Scatter(x=pd.DataFrame(states_df2.get_group(region))["Date"][:-1], y=pd.DataFrame(states_df2.get_group(region))["Forecasted_Cases_low_Daywise"], mode='lines', name='Forecasted Cases', line=dict(color='rgb(255, 150, 50)'), fill='tonexty', legendgroup="Forecasts", showlegend=False, visible=False))


    ######################
    fig.add_trace(go.Scatter(x=pd.DataFrame(states_df2.get_group(region))["Date"][:-1], y=pd.DataFrame(states_df2.get_group(region))["Active_Cases_Daywise"], mode='lines+markers', name='Active Cases', visible=False))
    fig.add_trace(go.Scatter(x=pd.DataFrame(states_df2.get_group(region))["Date"][:-1], y=pd.DataFrame(states_df2.get_group(region))["Forecasted_Active_Cases_Daywise"], mode='lines+markers', name='Forecasted Active Cases', line=dict(color='rgb(255, 100, 50)'), legendgroup="Forecasts", visible=False))
    fig.add_trace(go.Scatter(x=pd.DataFrame(states_df2.get_group(region))["Date"][:-1], y=pd.DataFrame(states_df2.get_group(region))["Forecasted_Active_Cases_high_Daywise"], mode='lines', name='Forecasted Active Cases', fill=None, line=dict(color='rgb(255, 150, 50)'), legendgroup="Forecasts", showlegend=False, visible=False))
    fig.add_trace(go.Scatter(x=pd.DataFrame(states_df2.get_group(region))["Date"][:-1], y=pd.DataFrame(states_df2.get_group(region))["Forecasted_Active_Cases_low_Daywise"], mode='lines', name='Forecasted Active Cases', line=dict(color='rgb(255, 150, 50)'), fill='tonexty', legendgroup="Forecasts", showlegend=False, visible=False))



    #fig.update_xaxes(tickangle=45, tickformat = '%d-%m')

    #Edit the layout
    fig.update_layout(template='plotly_white', legend=dict(x=0.01, y=0.95), margin=dict(l=20, r=20, t=50, b=20), hovermode='x unified', updatemenus=updatemenus)
    fig.update_layout(title='COVID-19 Cases Forecast - Total Cases', xaxis_title='Date', yaxis_title='Number of Cases')
    # fig.show()
    
    go_fig = fig.to_html(full_html=False, include_plotlyjs='cdn').replace('https://cdn.plot.ly/plotly-1.44.3.min.js', 'https://cdnjs.cloudflare.com/ajax/libs/plotly.js/1.44.4/plotly.min.js')
    
    return go_fig



def embbed_graph_mobile(region):
    updatemenus = list([    dict(active=0, buttons=list([
            dict(label = 'Confirmed Cases-Cumilative',
                 method = 'update',
                 args = [{'visible': [True, True, True, True, True, True, True, False, False, False, False, False, False, False, False, False, False, False]},
                         {'title': 'COVID-19 Cases Forecast - Total Cases',
                          'annotations': ''}]),
            dict(label = 'Confirmed Cases-New',
                 method = 'update',
                 args = [{'visible': [False, False, False, False, False, False, False, False, False, False, True, True, True, True, False, False, False, False]},
                         {'title': 'COVID-19 Cases Forecast - New Cases',
                          'annotations': ''}]),

            dict(label = 'Active Cases-Cumilative',
                 method = 'update',
                 args = [{'visible': [True, True, True, True, False, False, False, True, True, True, False, False, False, False, False, False, False, False]},
                         {'title': 'COVID-19 Cases Forecast - Total Cases',
                          'annotations': ''}]),
            dict(label = 'Active Cases-New',
                 method = 'update',
                 args = [{'visible': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, True, True]},
                         {'title': 'COVID-19 Cases Forecast - Active Cases',
                          'annotations': ''}]),        ]),                   

            x = 0.01,
            xanchor = 'left',
            y = 1.05,
            yanchor = 'top',    ),   ])

    df = pd.read_csv("COVID_Database.csv")
    states_df = df.groupby('Region')
    df = pd.read_csv("COVID_Forecasted.csv")
    states_df2 = df.groupby('Region')
    #Create the graph
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=pd.DataFrame(states_df2.get_group(region))["Date"][:-1], y=pd.DataFrame(states_df2.get_group(region))["Confirmed_Cases"], mode='lines', name='Confirmed Cases'))
    fig.add_trace(go.Scatter(x=pd.DataFrame(states_df2.get_group(region))["Date"][:-1], y=pd.DataFrame(states_df2.get_group(region))["Active_Cases"], mode='lines', name='Active Cases'))
    fig.add_trace(go.Scatter(x=pd.DataFrame(states_df2.get_group(region))["Date"][:-1], y=pd.DataFrame(states_df2.get_group(region))["Cured/Discharged"], mode='lines', name='Cured/Discharged'))
    fig.add_trace(go.Scatter(x=pd.DataFrame(states_df2.get_group(region))["Date"][:-1], y=pd.DataFrame(states_df2.get_group(region))["Death"], mode='lines', name='Deaths'))
    fig.add_trace(go.Scatter(x=pd.DataFrame(states_df2.get_group(region))["Date"][:-1], y=pd.DataFrame(states_df2.get_group(region))["Forecasted"], mode='lines', name='Forecasted Cases', line=dict(color='rgb(255, 100, 50)'), legendgroup="Forecasts"))
    fig.add_trace(go.Scatter(x=pd.DataFrame(states_df2.get_group(region))["Date"][:-1], y=pd.DataFrame(states_df2.get_group(region))["Forecasted_high"], mode='lines', name='Forecasted Cases', fill=None, line=dict(color='rgb(255, 150, 50)'), legendgroup="Forecasts", showlegend=False))
    fig.add_trace(go.Scatter(x=pd.DataFrame(states_df2.get_group(region))["Date"][:-1], y=pd.DataFrame(states_df2.get_group(region))["Forecasted_low"], mode='lines', name='Forecasted Cases', line=dict(color='rgb(255, 150, 50)'), fill='tonexty', legendgroup="Forecasts", showlegend=False))

    ######################
    fig.add_trace(go.Scatter(x=pd.DataFrame(states_df2.get_group(region))["Date"][:-1], y=pd.DataFrame(states_df2.get_group(region))["Forecasted_active"], mode='lines', name='Forecasted Active Cases', line=dict(color='rgb(255, 100, 50)'), legendgroup="Forecasts", visible=False))
    fig.add_trace(go.Scatter(x=pd.DataFrame(states_df2.get_group(region))["Date"][:-1], y=pd.DataFrame(states_df2.get_group(region))["Forecasted_active_high"], mode='lines', name='Forecasted Active Cases', fill=None, line=dict(color='rgb(255, 150, 50)'), legendgroup="Forecasts", showlegend=False, visible=False))
    fig.add_trace(go.Scatter(x=pd.DataFrame(states_df2.get_group(region))["Date"][:-1], y=pd.DataFrame(states_df2.get_group(region))["Forecasted_active_low"], mode='lines', name='Forecasted Active Cases', line=dict(color='rgb(255, 150, 50)'), fill='tonexty', legendgroup="Forecasts", showlegend=False, visible=False))



    fig.add_trace(go.Scatter(x=pd.DataFrame(states_df2.get_group(region))["Date"][:-1], y=pd.DataFrame(states_df2.get_group(region))["Confirmed_Cases_Daywise"], mode='lines', name='Confirmed Cases', visible=False))
    fig.add_trace(go.Scatter(x=pd.DataFrame(states_df2.get_group(region))["Date"][:-1], y=pd.DataFrame(states_df2.get_group(region))["Forecasted_Cases_Daywise"], mode='lines', name='Forecasted Cases', line=dict(color='rgb(255, 100, 50)'), legendgroup="Forecasts", visible=False))
    fig.add_trace(go.Scatter(x=pd.DataFrame(states_df2.get_group(region))["Date"][:-1], y=pd.DataFrame(states_df2.get_group(region))["Forecasted_Cases_high_Daywise"], mode='lines', name='Forecasted Cases', fill=None, line=dict(color='rgb(255, 150, 50)'), legendgroup="Forecasts", showlegend=False, visible=False))
    fig.add_trace(go.Scatter(x=pd.DataFrame(states_df2.get_group(region))["Date"][:-1], y=pd.DataFrame(states_df2.get_group(region))["Forecasted_Cases_low_Daywise"], mode='lines', name='Forecasted Cases', line=dict(color='rgb(255, 150, 50)'), fill='tonexty', legendgroup="Forecasts", showlegend=False, visible=False))


    ######################
    fig.add_trace(go.Scatter(x=pd.DataFrame(states_df2.get_group(region))["Date"][:-1], y=pd.DataFrame(states_df2.get_group(region))["Active_Cases_Daywise"], mode='lines', name='Active Cases', visible=False))
    fig.add_trace(go.Scatter(x=pd.DataFrame(states_df2.get_group(region))["Date"][:-1], y=pd.DataFrame(states_df2.get_group(region))["Forecasted_Active_Cases_Daywise"], mode='lines', name='Forecasted Active Cases', line=dict(color='rgb(255, 100, 50)'), legendgroup="Forecasts", visible=False))
    fig.add_trace(go.Scatter(x=pd.DataFrame(states_df2.get_group(region))["Date"][:-1], y=pd.DataFrame(states_df2.get_group(region))["Forecasted_Active_Cases_high_Daywise"], mode='lines', name='Forecasted Active Cases', fill=None, line=dict(color='rgb(255, 150, 50)'), legendgroup="Forecasts", showlegend=False, visible=False))
    fig.add_trace(go.Scatter(x=pd.DataFrame(states_df2.get_group(region))["Date"][:-1], y=pd.DataFrame(states_df2.get_group(region))["Forecasted_Active_Cases_low_Daywise"], mode='lines', name='Forecasted Active Cases', line=dict(color='rgb(255, 150, 50)'), fill='tonexty', legendgroup="Forecasts", showlegend=False, visible=False))



    #fig.update_xaxes(tickangle=45, tickformat = '%d-%m')

    #Edit the layout
    fig.update_layout(template='plotly_white', legend=dict(x=0.01, y=0.9, font=dict(size=10), borderwidth=0), margin=dict(l=0, r=1, t=80, b=20), hovermode='x unified', updatemenus=updatemenus)
    fig.update_layout(title='COVID-19 Cases Forecast - Total Cases', xaxis_title='Date', yaxis_title='Number of Cases')
    # fig.show()
    
    go_fig = fig.to_html(full_html=False, include_plotlyjs='cdn').replace('https://cdn.plot.ly/plotly-1.44.3.min.js', 'https://cdnjs.cloudflare.com/ajax/libs/plotly.js/1.44.4/plotly.min.js')
    
    return go_fig


def get_menu():
    web_element = '''<html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>Covid Forecasts</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<style>
/* Style the body */
body {
  font-family: Arial, Helvetica, sans-serif, Serif;
  margin: 0;
}

h1.Title {
  font-family: "Georgia, Times New Roman", Times, serif;
}

/* Header/Logo Title */
.header {
  padding: 0px;
  text-align: center;
  background: #333; //#1abc9c
  color: white;
  font-size: 20px;
  height: 15%;
}

/* Page Content */
.content {padding:20px;}

.navbar {
  overflow: hidden;
  background-color: #333;
  padding: 0px 0px 0px 0px;
  top: 70px;
  width: 100%;
}

.navbar a {
  float: left;
  font-size: 16px;
  color: white;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}

.dropdown {
  float: left;
  overflow: hidden;
}

.dropdown .dropbtn {
  font-size: 16px;  
  border: none;
  outline: none;
  color: white;
  padding: 14px 16px;
  background-color: inherit;
  font-family: inherit;
  margin: 0;
}

.navbar a:hover, .dropdown:hover .dropbtn {
  background-color: red;
}

.dropdown-content {
  display: none;
  position: absolute;
  background-color: #f9f9f9;
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 1;
}

.dropdown-content a {
  float: none;
  color: black;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
  text-align: left;
}

.dropdown-content a:hover {
  background-color: #ddd;
}

.dropdown:hover .dropdown-content {
  display: block;
}

table {
  width:100%;
}
table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
}
th, td {
  padding: 1px;
  text-align: left;
}
#t01 tr:nth-child(even) {
  background-color: #eee;
}
#t01 tr:nth-child(odd) {
 background-color: #fff;
}
#t01 th {
  background-color: #333;
  color: white;
}

footer {
   position: relative;
   bottom: 0;
   width: 100%;
   height: 30px;
   background-color: #333;
   color: white;
   text-align: center;
   margin: 0;
}

footer a {
   color: white;
   text-decoration: none;
}

</style>
<style id="plotly.js-style-global"></style><style id="plotly.js-style-modebar-0c9f6c"></style></head>
<body>

<div class="header">
  <h1 class="Title" style="font:Times New Roman; padding: 20px 0px 0px 0px; color: white;"> COVID-19 Forecasts </h1>
  <div class="navbar">
  <a href="http://covidforecasts.xyz/Home">Home</a>
  <a href="http://covidforecasts.xyz/forecast?region=World">World</a>
  <div class="dropdown">
    <button class="dropbtn">States (A-H)
      <i class="fa fa-caret-down"></i>
    </button>
    <div class="dropdown-content">
    <a href="http://covidforecasts.xyz/forecast?region=Andaman%20and%20Nicobar%20Islands">Andaman and Nicobar Islands</a>
    <a href="http://covidforecasts.xyz/forecast?region=Andhra%20Pradesh">Andhra Pradesh</a>
    <a href="http://covidforecasts.xyz/forecast?region=Arunachal%20Pradesh">Arunachal Pradesh</a>
    <a href="http://covidforecasts.xyz/forecast?region=Assam">Assam</a>
    <a href="http://covidforecasts.xyz/forecast?region=Bihar">Bihar</a>
    <a href="http://covidforecasts.xyz/forecast?region=Chandigarh">Chandigarh</a>
    <a href="http://covidforecasts.xyz/forecast?region=Chhattisgarh">Chhattisgarh</a>
    <a href="http://covidforecasts.xyz/forecast?region=Dadra%20and%20Nagar%20Haveli%20and%20Daman%20and%20Diu">Dadra and Nagar Haveli and Daman and Diu</a>
    <a href="http://covidforecasts.xyz/forecast?region=Delhi">Delhi</a>
    <a href="http://covidforecasts.xyz/forecast?region=Goa">Goa</a>
    <a href="http://covidforecasts.xyz/forecast?region=Gujarat">Gujarat</a>
    <a href="http://covidforecasts.xyz/forecast?region=Haryana">Haryana</a>
    <a href="http://covidforecasts.xyz/forecast?region=Himachal%20Pradesh">Himachal Pradesh</a>
    </div>
    </div>
    <div class="dropdown">
    <button class="dropbtn">States (J-P)
      <i class="fa fa-caret-down"></i>
    </button>
    <div class="dropdown-content">
    <a href="http://covidforecasts.xyz/forecast?region=Jammu%20and%20Kashmir">Jammu and Kashmir</a>
    <a href="http://covidforecasts.xyz/forecast?region=Jharkhand">Jharkhand</a>
    <a href="http://covidforecasts.xyz/forecast?region=Karnataka">Karnataka</a>
    <a href="http://covidforecasts.xyz/forecast?region=Kerala">Kerala</a>
    <a href="http://covidforecasts.xyz/forecast?region=Ladakh">Ladakh</a>
    <a href="http://covidforecasts.xyz/forecast?region=Madhya%20Pradesh">Madhya Pradesh</a>
    <a href="http://covidforecasts.xyz/forecast?region=Maharashtra">Maharashtra</a>
    <a href="http://covidforecasts.xyz/forecast?region=Manipur">Manipur</a>
    <a href="http://covidforecasts.xyz/forecast?region=Meghalaya">Meghalaya</a>
    <a href="http://covidforecasts.xyz/forecast?region=Mizoram">Mizoram</a>
    <a href="http://covidforecasts.xyz/forecast?region=Nagaland">Nagaland</a>
    <a href="http://covidforecasts.xyz/forecast?region=Odisha">Odisha</a>
    <a href="http://covidforecasts.xyz/forecast?region=Puducherry">Puducherry</a>
    <a href="http://covidforecasts.xyz/forecast?region=Punjab">Punjab</a>
    </div>
    </div>
    <div class="dropdown">
    <button class="dropbtn">States (R-Z)
      <i class="fa fa-caret-down"></i>
    </button>
    <div class="dropdown-content">
    <a href="http://covidforecasts.xyz/forecast?region=Rajasthan">Rajasthan</a>
    <a href="http://covidforecasts.xyz/forecast?region=Sikkim">Sikkim</a>
    <a href="http://covidforecasts.xyz/forecast?region=Tamil%20Nadu">Tamil Nadu</a>
    <a href="http://covidforecasts.xyz/forecast?region=Telangana">Telangana</a>
    <a href="http://covidforecasts.xyz/forecast?region=Tripura">Tripura</a>
    <a href="http://covidforecasts.xyz/forecast?region=Uttar%20Pradesh">Uttar Pradesh</a>
    <a href="http://covidforecasts.xyz/forecast?region=Uttarakhand">Uttarakhand</a>
    <a href="http://covidforecasts.xyz/forecast?region=West%20Bengal">West Bengal</a>
    </div>
  </div> 
  <a href="http://covidforecasts.xyz/About">About</a>
  <a href="http://covidforecasts.xyz/News">News</a>
  </div>
</body>'''

    return web_element


def get_menu_mobile():
    web_element = '''<html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>Covid Forecasts</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<style>
/* Style the body */
body {
  font-family: Arial, Helvetica, sans-serif, Serif;
  margin: 0;
}

h2.Title {
  font-family: "Georgia, Times New Roman", Times, serif;
}

/* Header/Logo Title */
.header {
  padding: 0px;
  text-align: center;
  background: #333; //#1abc9c
  color: white;
  font-size: 16px;
  height: 15%;
  width: 101%;
}

/* Page Content */
.content {padding:20px;}

.navbar {
  overflow: hidden;
  background-color: #333;
  padding: 0px 0px 0px 0px;
  top: 70px;
  width: 100%;
}

.navbar a {
  float: left;
  font-size: 12px;
  color: white;
  text-align: center;
  padding: 12px 14px 0px 5px;
  text-decoration: none;
}

.dropdown {
  float: left;
  overflow: hidden;
}

.dropdown .dropbtn {
  font-size: 12px;  
  border: none;
  outline: none;
  color: white;
  padding: 12px 0px 14px 5px;
  background-color: inherit;
  font-family: inherit;
  margin: 0;
}

.navbar a:hover, .dropdown:hover .dropbtn {
  background-color: red;
}

.dropdown-content {
  display: none;
  position: absolute;
  background-color: #f9f9f9;
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 1;
}

.dropdown-content a {
  float: none;
  color: black;
  padding: 12px 14px;
  text-decoration: none;
  display: block;
  text-align: left;
}

.dropdown-content a:hover {
  background-color: #ddd;
}

.dropdown:hover .dropdown-content {
  display: block;
}

table {
  width:100%;
}
table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
}
th, td {
  padding: 1px;
  text-align: left;
}
#t01 tr:nth-child(even) {
  background-color: #eee;
}
#t01 tr:nth-child(odd) {
 background-color: #fff;
}
#t01 th {
  background-color: #333;
  color: white;
}

footer {
   position: relative;
   bottom: 0;
   width: 100%;
   height: 30px;
   background-color: #333;
   color: white;
   text-align: center;
   margin: 0;
}

footer a {
   color: white;
   text-decoration: none;
}

</style>
<style id="plotly.js-style-global"></style><style id="plotly.js-style-modebar-9f480f"></style></head>
<body>

<div class="header">
  <h2 class="Title" style="font:Times New Roman; padding: 20px 0px 0px 0px; color: white;"> COVID-19 Forecasts </h2>
  <div class="navbar">
  <a style="padding: 12px 4px 14px 6px;" href="http://covidforecasts.xyz/Home">Home</a>
  <a style="padding: 12px 4px 14px 4px;" href="http://covidforecasts.xyz/forecast?region=World">World</a>
  <div class="dropdown">
    <button style="padding: 12px 4px 14px 2px;" class="dropbtn">States (A-H)
      <i class="fa fa-caret-down"></i>
    </button>
    <div class="dropdown-content">
    <a href="http://covidforecasts.xyz/forecast?region=Andaman%20and%20Nicobar%20Islands">Andaman and Nicobar Islands</a>
    <a href="http://covidforecasts.xyz/forecast?region=Andhra%20Pradesh">Andhra Pradesh</a>
    <a href="http://covidforecasts.xyz/forecast?region=Arunachal%20Pradesh">Arunachal Pradesh</a>
    <a href="http://covidforecasts.xyz/forecast?region=Assam">Assam</a>
    <a href="http://covidforecasts.xyz/forecast?region=Bihar">Bihar</a>
    <a href="http://covidforecasts.xyz/forecast?region=Chandigarh">Chandigarh</a>
    <a href="http://covidforecasts.xyz/forecast?region=Chhattisgarh">Chhattisgarh</a>
    <a href="http://covidforecasts.xyz/forecast?region=Dadra%20and%20Nagar%20Haveli%20and%20Daman%20and%20Diu">Dadra and Nagar Haveli and Daman and Diu</a>
    <a href="http://covidforecasts.xyz/forecast?region=Delhi">Delhi</a>
    <a href="http://covidforecasts.xyz/forecast?region=Goa">Goa</a>
    <a href="http://covidforecasts.xyz/forecast?region=Gujarat">Gujarat</a>
    <a href="http://covidforecasts.xyz/forecast?region=Haryana">Haryana</a>
    <a href="http://covidforecasts.xyz/forecast?region=Himachal%20Pradesh">Himachal Pradesh</a>
    </div>
    </div>
    <div class="dropdown">
    <button style="padding: 12px 4px 14px 2px;" class="dropbtn">States (J-P)
      <i class="fa fa-caret-down"></i>
    </button>
    <div class="dropdown-content">
    <a href="http://covidforecasts.xyz/forecast?region=Jammu%20and%20Kashmir">Jammu and Kashmir</a>
    <a href="http://covidforecasts.xyz/forecast?region=Jharkhand">Jharkhand</a>
    <a href="http://covidforecasts.xyz/forecast?region=Karnataka">Karnataka</a>
    <a href="http://covidforecasts.xyz/forecast?region=Kerala">Kerala</a>
    <a href="http://covidforecasts.xyz/forecast?region=Ladakh">Ladakh</a>
    <a href="http://covidforecasts.xyz/forecast?region=Madhya%20Pradesh">Madhya Pradesh</a>
    <a href="http://covidforecasts.xyz/forecast?region=Maharashtra">Maharashtra</a>
    <a href="http://covidforecasts.xyz/forecast?region=Manipur">Manipur</a>
    <a href="http://covidforecasts.xyz/forecast?region=Meghalaya">Meghalaya</a>
    <a href="http://covidforecasts.xyz/forecast?region=Mizoram">Mizoram</a>
    <a href="http://covidforecasts.xyz/forecast?region=Nagaland">Nagaland</a>
    <a href="http://covidforecasts.xyz/forecast?region=Odisha">Odisha</a>
    <a href="http://covidforecasts.xyz/forecast?region=Puducherry">Puducherry</a>
    <a href="http://covidforecasts.xyz/forecast?region=Punjab">Punjab</a>
    </div>
    </div>
    <div class="dropdown">
    <button style="padding: 12px 3px 14px 2px;" class="dropbtn">States (R-Z)
      <i class="fa fa-caret-down"></i>
    </button>
    <div class="dropdown-content">
    <a href="http://covidforecasts.xyz/forecast?region=Rajasthan">Rajasthan</a>
    <a href="http://covidforecasts.xyz/forecast?region=Sikkim">Sikkim</a>
    <a href="http://covidforecasts.xyz/forecast?region=Tamil%20Nadu">Tamil Nadu</a>
    <a href="http://covidforecasts.xyz/forecast?region=Telangana">Telangana</a>
    <a href="http://covidforecasts.xyz/forecast?region=Tripura">Tripura</a>
    <a href="http://covidforecasts.xyz/forecast?region=Uttar%20Pradesh">Uttar Pradesh</a>
    <a href="http://covidforecasts.xyz/forecast?region=Uttarakhand">Uttarakhand</a>
    <a href="http://covidforecasts.xyz/forecast?region=West%20Bengal">West Bengal</a>
    </div>
  </div> 
  <a style="padding: 12px 8px 14px 4px;" href="http://covidforecasts.xyz/News">News</a>
  </div> 
</div>
</body>'''
    return web_element


def get_about():

    return '''<html><head>
    <title>Covid Forecasts</title>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<style>
/* Style the body */
body {
  font-family: Arial, Helvetica, sans-serif, Serif;
  margin: 0;
}

h1.Title {
  font-family: "Georgia, Times New Roman", Times, serif;
}

/* Header/Logo Title */
.header {
  padding: 0px;
  text-align: center;
  background: #333; //#1abc9c
  color: white;
  font-size: 20px;
  height: 15%;
}

/* Page Content */
.content {padding:20px;}

.navbar {
  overflow: hidden;
  background-color: #333;
  padding: 0px 0px 0px 0px;
  top: 70px;
  width: 100%;
}

.navbar a {
  float: left;
  font-size: 16px;
  color: white;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}

.dropdown {
  float: left;
  overflow: hidden;
}

.dropdown .dropbtn {
  font-size: 16px;  
  border: none;
  outline: none;
  color: white;
  padding: 14px 16px;
  background-color: inherit;
  font-family: inherit;
  margin: 0;
}

.navbar a:hover, .dropdown:hover .dropbtn {
  background-color: red;
}

.dropdown-content {
  display: none;
  position: absolute;
  background-color: #f9f9f9;
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 1;
}

.dropdown-content a {
  float: none;
  color: black;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
  text-align: left;
}

.dropdown-content a:hover {
  background-color: #ddd;
}

.dropdown:hover .dropdown-content {
  display: block;
}

table {
  width:100%;
}
table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
}
th, td {
  padding: 1px;
  text-align: left;
}
#t01 tr:nth-child(even) {
  background-color: #eee;
}
#t01 tr:nth-child(odd) {
 background-color: #fff;
}
#t01 th {
  background-color: #333;
  color: white;
}
</style>
<style id="plotly.js-style-global"></style><style id="plotly.js-style-modebar-0c9f6c"></style></head>
<body>

<div class="header">
  <h1 class="Title" style="font:Times New Roman; padding: 20px 0px 0px 0px; color: white;"> COVID-19 Forecasts </h1>
  <div class="navbar">
  <a href="http://covidforecasts.xyz/Home">Home</a>
  <a href="http://covidforecasts.xyz/forecast?region=World">World</a>
  <div class="dropdown">
    <button class="dropbtn">States (A-H)
      <i class="fa fa-caret-down"></i>
    </button>
    <div class="dropdown-content">
    <a href="http://covidforecasts.xyz/forecast?region=Andaman%20and%20Nicobar%20Islands">Andaman and Nicobar Islands</a>
    <a href="http://covidforecasts.xyz/forecast?region=Andhra%20Pradesh">Andhra Pradesh</a>
    <a href="http://covidforecasts.xyz/forecast?region=Arunachal%20Pradesh">Arunachal Pradesh</a>
    <a href="http://covidforecasts.xyz/forecast?region=Assam">Assam</a>
    <a href="http://covidforecasts.xyz/forecast?region=Bihar">Bihar</a>
    <a href="http://covidforecasts.xyz/forecast?region=Chandigarh">Chandigarh</a>
    <a href="http://covidforecasts.xyz/forecast?region=Chhattisgarh">Chhattisgarh</a>
    <a href="http://covidforecasts.xyz/forecast?region=Dadra%20and%20Nagar%20Haveli%20and%20Daman%20and%20Diu">Dadra and Nagar Haveli and Daman and Diu</a>
    <a href="http://covidforecasts.xyz/forecast?region=Delhi">Delhi</a>
    <a href="http://covidforecasts.xyz/forecast?region=Goa">Goa</a>
    <a href="http://covidforecasts.xyz/forecast?region=Gujarat">Gujarat</a>
    <a href="http://covidforecasts.xyz/forecast?region=Haryana">Haryana</a>
    <a href="http://covidforecasts.xyz/forecast?region=Himachal%20Pradesh">Himachal Pradesh</a>
    </div>
    </div>
    <div class="dropdown">
    <button class="dropbtn">States (J-P)
      <i class="fa fa-caret-down"></i>
    </button>
    <div class="dropdown-content">
    <a href="http://covidforecasts.xyz/forecast?region=Jammu%20and%20Kashmir">Jammu and Kashmir</a>
    <a href="http://covidforecasts.xyz/forecast?region=Jharkhand">Jharkhand</a>
    <a href="http://covidforecasts.xyz/forecast?region=Karnataka">Karnataka</a>
    <a href="http://covidforecasts.xyz/forecast?region=Kerala">Kerala</a>
    <a href="http://covidforecasts.xyz/forecast?region=Ladakh">Ladakh</a>
    <a href="http://covidforecasts.xyz/forecast?region=Madhya%20Pradesh">Madhya Pradesh</a>
    <a href="http://covidforecasts.xyz/forecast?region=Maharashtra">Maharashtra</a>
    <a href="http://covidforecasts.xyz/forecast?region=Manipur">Manipur</a>
    <a href="http://covidforecasts.xyz/forecast?region=Meghalaya">Meghalaya</a>
    <a href="http://covidforecasts.xyz/forecast?region=Mizoram">Mizoram</a>
    <a href="http://covidforecasts.xyz/forecast?region=Nagaland">Nagaland</a>
    <a href="http://covidforecasts.xyz/forecast?region=Odisha">Odisha</a>
    <a href="http://covidforecasts.xyz/forecast?region=Puducherry">Puducherry</a>
    <a href="http://covidforecasts.xyz/forecast?region=Punjab">Punjab</a>
    </div>
    </div>
    <div class="dropdown">
    <button class="dropbtn">States (R-Z)
      <i class="fa fa-caret-down"></i>
    </button>
    <div class="dropdown-content">
    <a href="http://covidforecasts.xyz/forecast?region=Rajasthan">Rajasthan</a>
    <a href="http://covidforecasts.xyz/forecast?region=Sikkim">Sikkim</a>
    <a href="http://covidforecasts.xyz/forecast?region=Tamil%20Nadu">Tamil Nadu</a>
    <a href="http://covidforecasts.xyz/forecast?region=Telangana">Telangana</a>
    <a href="http://covidforecasts.xyz/forecast?region=Tripura">Tripura</a>
    <a href="http://covidforecasts.xyz/forecast?region=Uttar%20Pradesh">Uttar Pradesh</a>
    <a href="http://covidforecasts.xyz/forecast?region=Uttarakhand">Uttarakhand</a>
    <a href="http://covidforecasts.xyz/forecast?region=West%20Bengal">West Bengal</a>
    </div>
  </div> 
  <a href="http://covidforecasts.xyz/About">About</a>
  <a href="http://covidforecasts.xyz/News">News</a>
  </div>
</div>

<style>
div.Content{
font-size: 16px; 
padding: 20px 20px 20px 20px; 
width: 80%;
margin: auto;
text-align: justify;
text-justify: inter-word;
}

p{
font-size: 16px; 
padding: 0px 20px 0px 20px; 
margin: auto;
text-align: justify;
text-justify: inter-word;
}

i{
font-size: 16px;
}

footer {
   position: relative;
   bottom: 0;
   width: 100%;
   height: 30px;
   background-color: #333;
   color: white;
   text-align: center;
}

footer a {
   color: white;
   text-decoration: none;
}

p a {
color: blue;
text-decoration: none;
}

</style>
<script>
document.getElementById('mailtoid').click();
</script>
<body>
<div class="Content" ><br>
<h1 id="section1" style="margin-left: -50px">About</h1>
<h2>About the Model</h2>
<p>Like in case of all other things we believe in the saying simple is always the best. As such we have taken a Time-Series approach for forecasting the COVID-19 Pandemic.
We have used an ARIMA model to predict the COVID-19 Cases for the next few months and the model will be updated on a daily basis.
ARIMA, short for ‘AutoRegressive Integrated Moving Average’, is a forecasting algorithm based on the idea that the information in the past values of the time series can alone be used to predict the future values.  Any ‘non-seasonal’ time series that exhibits patterns and is not a random white noise can be modeled with ARIMA models.<br><br>
ARIMA takes into consideration the recent changes in data with more priority than the data say a month ago and as such, it works pretty well in forecasting COVID-19 Cases it has proven to forecast the Cases for the next 7 days with an error rate of +/-5%. Since the model is intended to be used for Short-term forecasts, It is not intended that this would be used for long-term predictions, as it is certainly not as sophisticated as complex <a href="https://bmcmedicine.biomedcentral.com/articles/10.1186/s12916-020-01628-4#:~:text=%5B1%5D%20is%20compartmental%20modelling%2C,%5Cbeta%20SI%2C%5Ckern0.">epidemiological models</a>.<br><br>
 Historical Performance & Baseline Comparison<br>
  Late June US Projection<br>
  Late May Projections</p><br>

<h2>Data Source and Forecasts</h2>
<p><i><strong>Our source:</strong></i> <a href="https://www.mohfw.gov.in/">Ministry of Health and Family Welfare, Government of India(MofW)</a>, Updates their database every day with accurate and confirmed data whose figures are being reconciled with <a href="https://www.icmr.gov.in/">ICMR</a> short for <a href="https://www.icmr.gov.in/">Indian Council of Medical Research, New Delhi</a>.<br>
For any further information on MoFW, you can reach them through the following mail address: <a href="technicalquery.covid19@gov.in">technicalquery.covid19@gov.in</a></p><br>
<p><i><strong>Forecasts:</strong></i> Forecasts for each Indian State, India as a country and the World will be updated on a daily basis and the model will be trained each on the recent changes in the data to accommodate all the real-world factors that affect the outcome of the forecasted cases which cannot be factored into the model.</p><br>
<h2>Assumptions</h2>
<p>Confidence Intervals</p><br>
<h2>Limitations</h2>
<p>We want to be as clear as possible regarding what our model can and cannot do. While we try our best to make accurate forecasts, no model is perfect. Here we present some of the known limitations of our model.</p><br>
<p><i><strong>Data Accuracy:</strong></i> A model is only as good as the data we feed it. If the data is not accurate, then it would be difficult to make accurate projections downstream.</p><br>
<p><i><strong>Lockdown fatigue / holidays:</strong></i> As per our analysis of the lockdown relaxation related impacts, an increasing number of people have been moving around in the weeks following a lockdown. This may contribute to an increase in infections in the weeks following the lockdown relaxation. Similarly, holidays & group activities specifically those without social distancing are a source of “superspreader” events, which we currently do not explicitly incorporate –This can be seen directly reflected in the graphs as a sharp spike following the opening of Lockdowns in each state where the actual confirmed cases overshadow the forecasts cases.</p><br>
<p><i><strong>Data frequency:</strong></i> Because our model uses only the daily case counts from each region to make forecasts, forecasts for those regions with minimal data (less than 1-2 weeks) or those regions with stagnant data such as regions with no new cases in the past few weeks cannot be forecasted.</p><br>
<p><i><strong>Day-of-week factors:</strong></i> We currently do not account for day-of-week factors in cases reported. i.e Cases reported on Sunday/Monday are about 60% of that of Tuesday-Thursday. So we expect on average that our projections will be higher than Sunday/Monday reports and lower than our Tuesday-Thursday reports. Also sometimes due to region & local restrictions there are delays in cases reported on a day which is added to the account of next day this is currently not considered in the model assumptions and for training as it is not possible to accurately identify the actual number of cases that were delayed in a day.</p><br>
<p><i><strong>Maximum Forecastable Timeline:</strong></i> Since this is a simple data dependent model the maximum rationally considerable forecasts for this particular subject is 30-31 days.</p><br>
<p><i><strong>End date:</strong></i> We are only making projections for 30-31 days/ 4-5 weeks ahead, but this does not mean that the epidemic will stop afterwards. Reported Cases may continue to rise even after we stop making projections. We currently plan on keeping the model updated on a daily basis until a cure has been found and the COVID-19 Pandemic ends.</p><br>
<h2>Who We Are</h2>
<p>This website is made by Tejas Haritsa V K, An <a href="https://iabac.org/">IABAC</a> Certified Data Scientist currently working as an AI Engineer at <a href="https://www.teleradtech.com/">TeleradTech</a>, Bengaluru, India.  Tejas Haritsa V K completed his Bachelor’s degree in Mechanical Engineering at the <a href="https://dbit.co.in/">Don Bosco Institute of Technology(DBIT), Bengaluru</a>. His expertise is in using machine learning to understand data and make accurate predictions. You can contact him on the mentioned channels on the <a href="http://covidforecasts.xyz/About#section2">Contact page</a>.</p><br>
<h2>Updates</h2>
<p> 06-08-2020: Added support for mobile devices </p><br>
<p> 08-08-2020: Added About page </p><br>
<p> 09-08-2020: Minor render adjustments for mobile devices </p><br>
<p> 09-08-2020: Added News Page </p><br>
<p> 10-08-2020: Added support for faster webpage loading </p><br>
<br>
<h1 id="section2" style="margin-left: -50px">Contact Us</h1>
<p>For any queries write to us on: <a href="mailto: covidforecasts@gmail.com" id="mailtoid">covidforecasts@gmail.com</a> </p>
<br>
</div>
</body>
</html>
<footer style="padding: 12px 0px 0px 0px;"> <a href="http://covidforecasts.xyz/About">About</a> &emsp; | &emsp; <a href="http://covidforecasts.xyz/About#section2">Contact Us</a> </footer> '''


def get_about_mobile():
    return '''<html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>Covid Forecasts</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<style>
/* Style the body */
body {
  font-family: Arial, Helvetica, sans-serif, Serif;
  margin: 0;
}

h2.Title {
  font-family: "Georgia, Times New Roman", Times, serif;
}

/* Header/Logo Title */
.header {
  padding: 0px;
  text-align: center;
  background: #333; //#1abc9c
  color: white;
  font-size: 16px;
  height: 15%;
  width: 101%;
}

/* Page Content */
.content {padding:20px;}

.navbar {
  overflow: hidden;
  background-color: #333;
  padding: 0px 0px 0px 0px;
  top: 70px;
  width: 100%;
}

.navbar a {
  float: left;
  font-size: 12px;
  color: white;
  text-align: center;
  padding: 12px 14px 0px 5px;
  text-decoration: none;
}

.dropdown {
  float: left;
  overflow: hidden;
}

.dropdown .dropbtn {
  font-size: 12px;  
  border: none;
  outline: none;
  color: white;
  padding: 12px 0px 14px 5px;
  background-color: inherit;
  font-family: inherit;
  margin: 0;
}

.navbar a:hover, .dropdown:hover .dropbtn {
  background-color: red;
}

.dropdown-content {
  display: none;
  position: absolute;
  background-color: #f9f9f9;
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 1;
}

.dropdown-content a {
  float: none;
  color: black;
  padding: 12px 14px;
  text-decoration: none;
  display: block;
  text-align: left;
}

.dropdown-content a:hover {
  background-color: #ddd;
}

.dropdown:hover .dropdown-content {
  display: block;
}

table {
  width:100%;
}
table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
}
th, td {
  padding: 1px;
  text-align: left;
}
#t01 tr:nth-child(even) {
  background-color: #eee;
}
#t01 tr:nth-child(odd) {
 background-color: #fff;
}
#t01 th {
  background-color: #333;
  color: white;
}
</style>
<style id="plotly.js-style-global"></style><style id="plotly.js-style-modebar-9f480f"></style></head>
<body>

<div class="header">
  <h2 class="Title" style="font:Times New Roman; padding: 20px 0px 0px 0px; color: white;"> COVID-19 Forecasts </h2>
  <div class="navbar">
  <a style="padding: 12px 4px 14px 6px;" href="http://covidforecasts.xyz/Home">Home</a>
  <a style="padding: 12px 4px 14px 4px;" href="http://covidforecasts.xyz/forecast?region=World">World</a>
  <div class="dropdown">
    <button style="padding: 12px 4px 14px 2px;" class="dropbtn">States (A-H)
      <i class="fa fa-caret-down"></i>
    </button>
    <div class="dropdown-content">
    <a href="http://covidforecasts.xyz/forecast?region=Andaman%20and%20Nicobar%20Islands">Andaman and Nicobar Islands</a>
    <a href="http://covidforecasts.xyz/forecast?region=Andhra%20Pradesh">Andhra Pradesh</a>
    <a href="http://covidforecasts.xyz/forecast?region=Arunachal%20Pradesh">Arunachal Pradesh</a>
    <a href="http://covidforecasts.xyz/forecast?region=Assam">Assam</a>
    <a href="http://covidforecasts.xyz/forecast?region=Bihar">Bihar</a>
    <a href="http://covidforecasts.xyz/forecast?region=Chandigarh">Chandigarh</a>
    <a href="http://covidforecasts.xyz/forecast?region=Chhattisgarh">Chhattisgarh</a>
    <a href="http://covidforecasts.xyz/forecast?region=Dadra%20and%20Nagar%20Haveli%20and%20Daman%20and%20Diu">Dadra and Nagar Haveli and Daman and Diu</a>
    <a href="http://covidforecasts.xyz/forecast?region=Delhi">Delhi</a>
    <a href="http://covidforecasts.xyz/forecast?region=Goa">Goa</a>
    <a href="http://covidforecasts.xyz/forecast?region=Gujarat">Gujarat</a>
    <a href="http://covidforecasts.xyz/forecast?region=Haryana">Haryana</a>
    <a href="http://covidforecasts.xyz/forecast?region=Himachal%20Pradesh">Himachal Pradesh</a>
    </div>
    </div>
    <div class="dropdown">
    <button style="padding: 12px 4px 14px 2px;" class="dropbtn">States (J-P)
      <i class="fa fa-caret-down"></i>
    </button>
    <div class="dropdown-content">
    <a href="http://covidforecasts.xyz/forecast?region=Jammu%20and%20Kashmir">Jammu and Kashmir</a>
    <a href="http://covidforecasts.xyz/forecast?region=Jharkhand">Jharkhand</a>
    <a href="http://covidforecasts.xyz/forecast?region=Karnataka">Karnataka</a>
    <a href="http://covidforecasts.xyz/forecast?region=Kerala">Kerala</a>
    <a href="http://covidforecasts.xyz/forecast?region=Ladakh">Ladakh</a>
    <a href="http://covidforecasts.xyz/forecast?region=Madhya%20Pradesh">Madhya Pradesh</a>
    <a href="http://covidforecasts.xyz/forecast?region=Maharashtra">Maharashtra</a>
    <a href="http://covidforecasts.xyz/forecast?region=Manipur">Manipur</a>
    <a href="http://covidforecasts.xyz/forecast?region=Meghalaya">Meghalaya</a>
    <a href="http://covidforecasts.xyz/forecast?region=Mizoram">Mizoram</a>
    <a href="http://covidforecasts.xyz/forecast?region=Nagaland">Nagaland</a>
    <a href="http://covidforecasts.xyz/forecast?region=Odisha">Odisha</a>
    <a href="http://covidforecasts.xyz/forecast?region=Puducherry">Puducherry</a>
    <a href="http://covidforecasts.xyz/forecast?region=Punjab">Punjab</a>
    </div>
    </div>
    <div class="dropdown">
    <button style="padding: 12px 3px 14px 2px;" class="dropbtn">States (R-Z)
      <i class="fa fa-caret-down"></i>
    </button>
    <div class="dropdown-content">
    <a href="http://covidforecasts.xyz/forecast?region=Rajasthan">Rajasthan</a>
    <a href="http://covidforecasts.xyz/forecast?region=Sikkim">Sikkim</a>
    <a href="http://covidforecasts.xyz/forecast?region=Tamil%20Nadu">Tamil Nadu</a>
    <a href="http://covidforecasts.xyz/forecast?region=Telangana">Telangana</a>
    <a href="http://covidforecasts.xyz/forecast?region=Tripura">Tripura</a>
    <a href="http://covidforecasts.xyz/forecast?region=Uttar%20Pradesh">Uttar Pradesh</a>
    <a href="http://covidforecasts.xyz/forecast?region=Uttarakhand">Uttarakhand</a>
    <a href="http://covidforecasts.xyz/forecast?region=West%20Bengal">West Bengal</a>
    </div>
  </div> 
  <a style="padding: 12px 8px 14px 4px;" href="http://covidforecasts.xyz/News">News</a>
  </div> 
</div>

<style>
div.Content{
font-size: 14px; 
padding: 20px 20px 20px 20px; 
width: 90%;
margin: auto;
text-align: justify;
text-justify: inter-word;
}

p{
font-size: 14px; 
padding: 0px 20px 0px 20px; 
margin: auto;
text-align: justify;
text-justify: inter-word;
}

i{
font-size: 14px;
}

footer {
   position: relative;
   bottom: 0;
   width: 100%;
   height: 30px;
   background-color: #333;
   color: white;
   text-align: center;
}

footer a {
   color: white;
   text-decoration: none;
}

p a {
color: blue;
text-decoration: none;
}

</style>
<script>
document.getElementById('mailtoid').click();
</script>
<body>
<div class="Content" ><br>
<h1 id="section1" style="margin-left: -10px">About</h1>
<h2>About the Model</h2>
<p>Like in case of all other things we believe in the saying simple is always the best. As such we have taken a Time-Series approach for forecasting the COVID-19 Pandemic.
We have used an ARIMA model to predict the COVID-19 Cases for the next few months and the model will be updated on a daily basis.
ARIMA, short for ‘AutoRegressive Integrated Moving Average’, is a forecasting algorithm based on the idea that the information in the past values of the time series can alone be used to predict the future values.  Any ‘non-seasonal’ time series that exhibits patterns and is not a random white noise can be modeled with ARIMA models.<br><br>
ARIMA takes into consideration the recent changes in data with more priority than the data say a month ago and as such, it works pretty well in forecasting COVID-19 Cases it has proven to forecast the Cases for the next 7 days with an error rate of +/-5%. Since the model is intended to be used for Short-term forecasts, It is not intended that this would be used for long-term predictions, as it is certainly not as sophisticated as complex <a href="https://bmcmedicine.biomedcentral.com/articles/10.1186/s12916-020-01628-4#:~:text=%5B1%5D%20is%20compartmental%20modelling%2C,%5Cbeta%20SI%2C%5Ckern0.">epidemiological models</a>.<br><br>
 Historical Performance & Baseline Comparison<br>
  Late June US Projection<br>
  Late May Projections</p><br>

<h2>Data Source and Forecasts</h2>
<p><i><strong>Our source:</strong></i> <a href="https://www.mohfw.gov.in/">Ministry of Health and Family Welfare, Government of India(MofW)</a>, Updates their database every day with accurate and confirmed data whose figures are being reconciled with <a href="https://www.icmr.gov.in/">ICMR</a> short for <a href="https://www.icmr.gov.in/">Indian Council of Medical Research, New Delhi</a>.<br>
For any further information on MoFW, you can reach them through the following mail address: <a href="technicalquery.covid19@gov.in">technicalquery.covid19@gov.in</a></p><br>
<p><i><strong>Forecasts:</strong></i> Forecasts for each Indian State, India as a country and the World will be updated on a daily basis and the model will be trained each on the recent changes in the data to accommodate all the real-world factors that affect the outcome of the forecasted cases which cannot be factored into the model.</p><br>
<h2>Assumptions</h2>
<p>Confidence Intervals</p><br>
<h2>Limitations</h2>
<p>We want to be as clear as possible regarding what our model can and cannot do. While we try our best to make accurate forecasts, no model is perfect. Here we present some of the known limitations of our model.</p><br>
<p><i><strong>Data Accuracy:</strong></i> A model is only as good as the data we feed it. If the data is not accurate, then it would be difficult to make accurate projections downstream.</p><br>
<p><i><strong>Lockdown fatigue / holidays:</strong></i> As per our analysis of the lockdown relaxation related impacts, an increasing number of people have been moving around in the weeks following a lockdown. This may contribute to an increase in infections in the weeks following the lockdown relaxation. Similarly, holidays & group activities specifically those without social distancing are a source of “superspreader” events, which we currently do not explicitly incorporate –This can be seen directly reflected in the graphs as a sharp spike following the opening of Lockdowns in each state where the actual confirmed cases overshadow the forecasts cases.</p><br>
<p><i><strong>Data frequency:</strong></i> Because our model uses only the daily case counts from each region to make forecasts, forecasts for those regions with minimal data (less than 1-2 weeks) or those regions with stagnant data such as regions with no new cases in the past few weeks cannot be forecasted.</p><br>
<p><i><strong>Day-of-week factors:</strong></i> We currently do not account for day-of-week factors in cases reported. i.e Cases reported on Sunday/Monday are about 60% of that of Tuesday-Thursday. So we expect on average that our projections will be higher than Sunday/Monday reports and lower than our Tuesday-Thursday reports. Also sometimes due to region & local restrictions there are delays in cases reported on a day which is added to the account of next day this is currently not considered in the model assumptions and for training as it is not possible to accurately identify the actual number of cases that were delayed in a day.</p><br>
<p><i><strong>Maximum Forecastable Timeline:</strong></i> Since this is a simple data dependent model the maximum rationally considerable forecasts for this particular subject is 30-31 days.</p><br>
<p><i><strong>End date:</strong></i> We are only making projections for 30-31 days/ 4-5 weeks ahead, but this does not mean that the epidemic will stop afterwards. Reported Cases may continue to rise even after we stop making projections. We currently plan on keeping the model updated on a daily basis until a cure has been found and the COVID-19 Pandemic ends.</p><br>
<h2>Who We Are</h2>
<p>This website is made by Tejas Haritsa V K, An <a href="https://iabac.org/">IABAC</a> Certified Data Scientist currently working as an AI Engineer at <a href="https://www.teleradtech.com/">TeleradTech</a>, Bengaluru, India.  Tejas Haritsa V K completed his Bachelor’s degree in Mechanical Engineering at the <a href="https://dbit.co.in/">Don Bosco Institute of Technology(DBIT), Bengaluru</a>. His expertise is in using machine learning to understand data and make accurate predictions. You can contact him on the mentioned channels on the <a href="http://covidforecasts.xyz/About#section2">Contact page</a>.</p><br>
<h2>Updates</h2>
<p> 06-08-2020: Added support for mobile devices </p><br>
<p> 08-08-2020: Added About page </p><br>
<p> 09-08-2020: Minor render adjustments for mobile devices </p><br>
<p> 09-08-2020: Added News Page </p><br>
<p> 10-08-2020: Added support for faster webpage loading </p><br>
<br>
<h1 id="section2" style="margin-left: -10px">Contact Us</h1>
<p>For any queries write to us on: <a href="mailto: covidforecasts@gmail.com" id="mailtoid">covidforecasts@gmail.com</a> </p>
<br>
</div>
</body>
</html>
<footer style="padding: 12px 0px 0px 0px;"> <a href="http://covidforecasts.xyz/About">About</a> &emsp; | &emsp; <a href="http://covidforecasts.xyz/About#section2">Contact Us</a> </footer>'''



def get_news():
    return '''<html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>Covid Forecasts</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<style>
/* Style the body */
body {
  font-family: Arial, Helvetica, sans-serif, Serif;
  margin: 0;
}

h1.Title {
  font-family: "Georgia, Times New Roman", Times, serif;
}

/* Header/Logo Title */
.header {
  padding: 0px;
  text-align: center;
  background: #333; //#1abc9c
  color: white;
  font-size: 20px;
  height: 15%;
}

/* Page Content */
.content {padding:20px;}

.navbar {
  overflow: hidden;
  background-color: #333;
  padding: 0px 0px 0px 0px;
  top: 70px;
  width: 100%;
}

.navbar a {
  float: left;
  font-size: 16px;
  color: white;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}

.dropdown {
  float: left;
  overflow: hidden;
}

.dropdown .dropbtn {
  font-size: 16px;  
  border: none;
  outline: none;
  color: white;
  padding: 14px 16px;
  background-color: inherit;
  font-family: inherit;
  margin: 0;
}

.navbar a:hover, .dropdown:hover .dropbtn {
  background-color: red;
}

.dropdown-content {
  display: none;
  position: absolute;
  background-color: #f9f9f9;
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 1;
}

.dropdown-content a {
  float: none;
  color: black;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
  text-align: left;
}

.dropdown-content a:hover {
  background-color: #ddd;
}

.dropdown:hover .dropdown-content {
  display: block;
}

table {
  width:100%;
}
table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
}
th, td {
  padding: 1px;
  text-align: left;
}
#t01 tr:nth-child(even) {
  background-color: #eee;
}
#t01 tr:nth-child(odd) {
 background-color: #fff;
}
#t01 th {
  background-color: #333;
  color: white;
}
</style>
<style id="plotly.js-style-global"></style><style id="plotly.js-style-modebar-0c9f6c"></style></head>
<body>

<div class="header">
  <h1 class="Title" style="font:Times New Roman; padding: 20px 0px 0px 0px; color: white;"> COVID-19 Forecasts </h1>
  <div class="navbar">
  <a href="http://covidforecasts.xyz/Home">Home</a>
  <a href="http://covidforecasts.xyz/forecast?region=World">World</a>
  <div class="dropdown">
    <button class="dropbtn">States (A-H)
      <i class="fa fa-caret-down"></i>
    </button>
    <div class="dropdown-content">
    <a href="http://covidforecasts.xyz/forecast?region=Andaman%20and%20Nicobar%20Islands">Andaman and Nicobar Islands</a>
    <a href="http://covidforecasts.xyz/forecast?region=Andhra%20Pradesh">Andhra Pradesh</a>
    <a href="http://covidforecasts.xyz/forecast?region=Arunachal%20Pradesh">Arunachal Pradesh</a>
    <a href="http://covidforecasts.xyz/forecast?region=Assam">Assam</a>
    <a href="http://covidforecasts.xyz/forecast?region=Bihar">Bihar</a>
    <a href="http://covidforecasts.xyz/forecast?region=Chandigarh">Chandigarh</a>
    <a href="http://covidforecasts.xyz/forecast?region=Chhattisgarh">Chhattisgarh</a>
    <a href="http://covidforecasts.xyz/forecast?region=Dadra%20and%20Nagar%20Haveli%20and%20Daman%20and%20Diu">Dadra and Nagar Haveli and Daman and Diu</a>
    <a href="http://covidforecasts.xyz/forecast?region=Delhi">Delhi</a>
    <a href="http://covidforecasts.xyz/forecast?region=Goa">Goa</a>
    <a href="http://covidforecasts.xyz/forecast?region=Gujarat">Gujarat</a>
    <a href="http://covidforecasts.xyz/forecast?region=Haryana">Haryana</a>
    <a href="http://covidforecasts.xyz/forecast?region=Himachal%20Pradesh">Himachal Pradesh</a>
    </div>
    </div>
    <div class="dropdown">
    <button class="dropbtn">States (J-P)
      <i class="fa fa-caret-down"></i>
    </button>
    <div class="dropdown-content">
    <a href="http://covidforecasts.xyz/forecast?region=Jammu%20and%20Kashmir">Jammu and Kashmir</a>
    <a href="http://covidforecasts.xyz/forecast?region=Jharkhand">Jharkhand</a>
    <a href="http://covidforecasts.xyz/forecast?region=Karnataka">Karnataka</a>
    <a href="http://covidforecasts.xyz/forecast?region=Kerala">Kerala</a>
    <a href="http://covidforecasts.xyz/forecast?region=Ladakh">Ladakh</a>
    <a href="http://covidforecasts.xyz/forecast?region=Madhya%20Pradesh">Madhya Pradesh</a>
    <a href="http://covidforecasts.xyz/forecast?region=Maharashtra">Maharashtra</a>
    <a href="http://covidforecasts.xyz/forecast?region=Manipur">Manipur</a>
    <a href="http://covidforecasts.xyz/forecast?region=Meghalaya">Meghalaya</a>
    <a href="http://covidforecasts.xyz/forecast?region=Mizoram">Mizoram</a>
    <a href="http://covidforecasts.xyz/forecast?region=Nagaland">Nagaland</a>
    <a href="http://covidforecasts.xyz/forecast?region=Odisha">Odisha</a>
    <a href="http://covidforecasts.xyz/forecast?region=Puducherry">Puducherry</a>
    <a href="http://covidforecasts.xyz/forecast?region=Punjab">Punjab</a>
    </div>
    </div>
    <div class="dropdown">
    <button class="dropbtn">States (R-Z)
      <i class="fa fa-caret-down"></i>
    </button>
    <div class="dropdown-content">
    <a href="http://covidforecasts.xyz/forecast?region=Rajasthan">Rajasthan</a>
    <a href="http://covidforecasts.xyz/forecast?region=Sikkim">Sikkim</a>
    <a href="http://covidforecasts.xyz/forecast?region=Tamil%20Nadu">Tamil Nadu</a>
    <a href="http://covidforecasts.xyz/forecast?region=Telangana">Telangana</a>
    <a href="http://covidforecasts.xyz/forecast?region=Tripura">Tripura</a>
    <a href="http://covidforecasts.xyz/forecast?region=Uttar%20Pradesh">Uttar Pradesh</a>
    <a href="http://covidforecasts.xyz/forecast?region=Uttarakhand">Uttarakhand</a>
    <a href="http://covidforecasts.xyz/forecast?region=West%20Bengal">West Bengal</a>
    </div>
  </div> 
  <a href="http://covidforecasts.xyz/About">About</a>
  </div>
</div>

<style>
div.Content{
font-size: 16px; 
padding: 20px 20px 20px 20px; 
width: 80%;
margin: auto;
text-align: justify;
text-justify: inter-word;
}

p{
font-size: 16px; 
padding: 0px 20px 0px 20px; 
margin: auto;
text-align: justify;
text-justify: inter-word;
}

i{
font-size: 16px;
}

footer {
   position: relative;
   bottom: 0;
   width: 100%;
   height: 30px;
   background-color: #333;
   color: white;
   text-align: center;
}

footer a {
   color: white;
   text-decoration: none;
}

p a {
color: blue;
text-decoration: none;
}

</style>
<body>
<div class="Content" >
<h1 style="margin-left: -50px">News</h1>

<script>
$('#rightpanel').load('https://indianexpress.com/?s=corona+virus #row');
$('#append_breaking_box').style.display="none";
</script>
<br>

<div id="iframe" style="width: 100%; margin-left: auto; margin-right: auto;">
    <h3><a href="https://indianexpress.com/?s=corona+virus"> The Indian Express</a></h3><br>
	<iframe src="https://indianexpress.com/?s=corona+virus" title="The Indian Express" scrolling="yes" style="width: 100%; height: 500px; margin-top: 0px;"></iframe>
	
	<br><br><br>
	
    <h3><a href="https://timesofindia.indiatimes.com/coronavirus">Times Of India</a></h3><br>
	<iframe sandbox="" src="https://timesofindia.indiatimes.com/coronavirus" title="Times of India" scrolling="yes" style="width: 100%; height: 500px; margin-top: 0px;"></iframe> 
	
	<br><br><br>
	
    <h3><a href="https://www.hindustantimes.com/coronavirus/">Hindustan Times</a></h3><br>
	<iframe src="https://www.hindustantimes.com/coronavirus/" title="Hindustan Times" scrolling="yes" style="width: 100%; height: 500px; margin-top: 0px;"></iframe>
</div>
<br>
<h4> Disclaimer: All the news feed seen on this page belngs to & owned by their respective organizations and we do not own them. All content used here are to be considered as fair usage under fair usage policy. </h4>
<br>
</div>
</body>
</html>
<footer style="padding: 12px 0px 0px 0px;"> <a href="http://covidforecasts.xyz/About">About</a> &emsp; | &emsp; <a href="http://covidforecasts.xyz/About#section2">Contact Us</a> </footer>'''



def get_news_mobile():
    return '''<html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>Covid Forecasts</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<style>
/* Style the body */
body {
  font-family: Arial, Helvetica, sans-serif, Serif;
  margin: 0;
}

h2.Title {
  font-family: "Georgia, Times New Roman", Times, serif;
}

/* Header/Logo Title */
.header {
  padding: 0px;
  text-align: center;
  background: #333; //#1abc9c
  color: white;
  font-size: 16px;
  height: 15%;
  width: 101%;
}

/* Page Content */
.content {padding:20px;}

.navbar {
  overflow: hidden;
  background-color: #333;
  padding: 0px 0px 0px 0px;
  top: 70px;
  width: 100%;
}

.navbar a {
  float: left;
  font-size: 12px;
  color: white;
  text-align: center;
  padding: 12px 14px 0px 5px;
  text-decoration: none;
}

.dropdown {
  float: left;
  overflow: hidden;
}

.dropdown .dropbtn {
  font-size: 12px;  
  border: none;
  outline: none;
  color: white;
  padding: 12px 0px 14px 5px;
  background-color: inherit;
  font-family: inherit;
  margin: 0;
}

.navbar a:hover, .dropdown:hover .dropbtn {
  background-color: red;
}

.dropdown-content {
  display: none;
  position: absolute;
  background-color: #f9f9f9;
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 1;
}

.dropdown-content a {
  float: none;
  color: black;
  padding: 12px 14px;
  text-decoration: none;
  display: block;
  text-align: left;
}

.dropdown-content a:hover {
  background-color: #ddd;
}

.dropdown:hover .dropdown-content {
  display: block;
}

table {
  width:100%;
}
table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
}
th, td {
  padding: 1px;
  text-align: left;
}
#t01 tr:nth-child(even) {
  background-color: #eee;
}
#t01 tr:nth-child(odd) {
 background-color: #fff;
}
#t01 th {
  background-color: #333;
  color: white;
}

footer {
   position: relative;
   bottom: 0;
   width: 100%;
   height: 30px;
   background-color: #333;
   color: white;
   text-align: center;
   margin: 0;
}

footer a {
   color: white;
   text-decoration: none;
}

</style>
<style id="plotly.js-style-global"></style><style id="plotly.js-style-modebar-9f480f"></style></head>
<body>

<div class="header">
  <h2 class="Title" style="font:Times New Roman; padding: 20px 0px 0px 0px; color: white;"> COVID-19 Forecasts </h2>
  <div class="navbar">
  <a style="padding: 12px 4px 14px 6px;" href="http://covidforecasts.xyz/Home">Home</a>
  <a style="padding: 12px 4px 14px 4px;" href="http://covidforecasts.xyz/forecast?region=World">World</a>
  <div class="dropdown">
    <button style="padding: 12px 4px 14px 2px;" class="dropbtn">States (A-H)
      <i class="fa fa-caret-down"></i>
    </button>
    <div class="dropdown-content">
    <a href="http://covidforecasts.xyz/forecast?region=Andaman%20and%20Nicobar%20Islands">Andaman and Nicobar Islands</a>
    <a href="http://covidforecasts.xyz/forecast?region=Andhra%20Pradesh">Andhra Pradesh</a>
    <a href="http://covidforecasts.xyz/forecast?region=Arunachal%20Pradesh">Arunachal Pradesh</a>
    <a href="http://covidforecasts.xyz/forecast?region=Assam">Assam</a>
    <a href="http://covidforecasts.xyz/forecast?region=Bihar">Bihar</a>
    <a href="http://covidforecasts.xyz/forecast?region=Chandigarh">Chandigarh</a>
    <a href="http://covidforecasts.xyz/forecast?region=Chhattisgarh">Chhattisgarh</a>
    <a href="http://covidforecasts.xyz/forecast?region=Dadra%20and%20Nagar%20Haveli%20and%20Daman%20and%20Diu">Dadra and Nagar Haveli and Daman and Diu</a>
    <a href="http://covidforecasts.xyz/forecast?region=Delhi">Delhi</a>
    <a href="http://covidforecasts.xyz/forecast?region=Goa">Goa</a>
    <a href="http://covidforecasts.xyz/forecast?region=Gujarat">Gujarat</a>
    <a href="http://covidforecasts.xyz/forecast?region=Haryana">Haryana</a>
    <a href="http://covidforecasts.xyz/forecast?region=Himachal%20Pradesh">Himachal Pradesh</a>
    </div>
    </div>
    <div class="dropdown">
    <button style="padding: 12px 4px 14px 2px;" class="dropbtn">States (J-P)
      <i class="fa fa-caret-down"></i>
    </button>
    <div class="dropdown-content">
    <a href="http://covidforecasts.xyz/forecast?region=Jammu%20and%20Kashmir">Jammu and Kashmir</a>
    <a href="http://covidforecasts.xyz/forecast?region=Jharkhand">Jharkhand</a>
    <a href="http://covidforecasts.xyz/forecast?region=Karnataka">Karnataka</a>
    <a href="http://covidforecasts.xyz/forecast?region=Kerala">Kerala</a>
    <a href="http://covidforecasts.xyz/forecast?region=Ladakh">Ladakh</a>
    <a href="http://covidforecasts.xyz/forecast?region=Madhya%20Pradesh">Madhya Pradesh</a>
    <a href="http://covidforecasts.xyz/forecast?region=Maharashtra">Maharashtra</a>
    <a href="http://covidforecasts.xyz/forecast?region=Manipur">Manipur</a>
    <a href="http://covidforecasts.xyz/forecast?region=Meghalaya">Meghalaya</a>
    <a href="http://covidforecasts.xyz/forecast?region=Mizoram">Mizoram</a>
    <a href="http://covidforecasts.xyz/forecast?region=Nagaland">Nagaland</a>
    <a href="http://covidforecasts.xyz/forecast?region=Odisha">Odisha</a>
    <a href="http://covidforecasts.xyz/forecast?region=Puducherry">Puducherry</a>
    <a href="http://covidforecasts.xyz/forecast?region=Punjab">Punjab</a>
    </div>
    </div>
    <div class="dropdown">
    <button style="padding: 12px 3px 14px 2px;" class="dropbtn">States (R-Z)
      <i class="fa fa-caret-down"></i>
    </button>
    <div class="dropdown-content">
    <a href="http://covidforecasts.xyz/forecast?region=Rajasthan">Rajasthan</a>
    <a href="http://covidforecasts.xyz/forecast?region=Sikkim">Sikkim</a>
    <a href="http://covidforecasts.xyz/forecast?region=Tamil%20Nadu">Tamil Nadu</a>
    <a href="http://covidforecasts.xyz/forecast?region=Telangana">Telangana</a>
    <a href="http://covidforecasts.xyz/forecast?region=Tripura">Tripura</a>
    <a href="http://covidforecasts.xyz/forecast?region=Uttar%20Pradesh">Uttar Pradesh</a>
    <a href="http://covidforecasts.xyz/forecast?region=Uttarakhand">Uttarakhand</a>
    <a href="http://covidforecasts.xyz/forecast?region=West%20Bengal">West Bengal</a>
    </div>
  </div> 
  <a style="padding: 12px 8px 14px 4px;" href="http://covidforecasts.xyz/News">News</a>
  </div> 
</div>
</body>

<div class="Content" >
<h1 style="margin-left: -10px">News</h1>

<script>
$('#rightpanel').load('https://indianexpress.com/?s=corona+virus #row');
$('#append_breaking_box').style.display="none";
</script>
<br>

<div id="iframe" style="width: 100%; margin-left: auto; margin-right: auto;">
    <h3><a href="https://indianexpress.com/?s=corona+virus">Indian Express</a></h3><br>
	<iframe src="https://indianexpress.com/?s=corona+virus" title="Indian Express" scrolling="yes" style="width: 100%; height: 500px; margin-top: 0px;"></iframe>
	
	<br><br><br>
	
    <h3><a href="https://timesofindia.indiatimes.com/coronavirus">Times Of India</a></h3><br>
	<iframe sandbox="" src="https://timesofindia.indiatimes.com/coronavirus" title="Times of India" scrolling="yes" style="width: 100%; height: 500px; margin-top: 0px;"></iframe> 
	
	<br><br><br>
	
    <h3><a href="https://www.hindustantimes.com/coronavirus/">Hindustan Times</a></h3><br>
	<iframe src="https://www.hindustantimes.com/coronavirus/" title="Hindustan Times" scrolling="yes" style="width: 100%; height: 500px; margin-top: 0px;"></iframe>
</div>
<br>
<h4> Disclaimer: All the news feed seen on this page belngs to & owned by their respective organizations and we do not own them. All content used here are to be considered as fair usage under fair usage policy. </h4>
<br>
</div>
</body>
</html>
<footer style="padding: 12px 0px 0px 0px;"> <a href="http://covidforecasts.xyz/About">About</a> &emsp; | &emsp; <a href="http://covidforecasts.xyz/About#section2">Contact Us</a> </footer>'''




def add_cases_compare(region, as_on, yesterday):
    df = pd.read_csv("Forecast.csv")
    yesterday_forecast = int(df[df.Region==region].iloc[0,-2])
    df = pd.read_csv("COVID_Forecasted.csv")
    df = df[df.Region==region]
    try:
        today_forecast = int(df.Forecasted[df.Date==as_on.strftime('%d-%m-%Y')].iloc[1])
    except:
        today_forecast = int(df.Forecasted[df.Date==as_on.strftime('%d-%m-%Y')].iloc[0])
    return '''<p style="font:Helvetica; color:#fff; font-size: 20px; position: absolute;  right: 10px;  top: 35px;  z-index: 1; text-align:right; line-height: 1.0; padding: 0px 10px 0px 0px "> Today's Forecast: <strong style="font-size: 24px;">{}</strong> <br> </p> 
    <p style="font:Helvetica; color:#fff;  position: absolute;  right: 10px;  top: 65px;  z-index: 1; text-align:right; line-height: 1.0;"> Our Forcasted Cases Yesterday: <strong style="font-size: 18px;">{}</strong> <br> Confirmed Cases Yesterday: <strong style="font-size: 16px;">{}</strong></p>'''.format(today_forecast, yesterday_forecast, int(yesterday))


def add_cases_compare_mobile(region, as_on, yesterday):
    df = pd.read_csv("Forecast.csv")
    yesterday_forecast = int(df[df.Region==region].iloc[0,-2])
    df = pd.read_csv("COVID_Forecasted.csv")
    df = df[df.Region==region]
    try:
        today_forecast = int(df.Forecasted[df.Date==as_on.strftime('%d-%m-%Y')].iloc[1])
    except:
        today_forecast = int(df.Forecasted[df.Date==as_on.strftime('%d-%m-%Y')].iloc[0])
    return '''<p style="font:Helvetica; color:black; font-size: 12px; position: absolute;  right: 10px;  top: 118px;  z-index: -1; text-align:right; line-height: 1.0; padding: 0px 10px 0px 0px "> <b>Today's Forecast: <strong style="font-size: 14px;">{}</strong></b> <br> </p> 
    <p style="font:Helvetica; color:black; font-size: 10px; position: absolute;  right: 10px;  top: 134px;  z-index: -1; text-align:right; line-height: 1.1;"> <b> Our Forcasted Cases Yesterday: <strong style="font-size: 12px;">{}</strong> </b> <br> <b> Confirmed Cases Yesterday: <strong style="font-size: 12px;">{}</strong> </b> </p>'''.format(today_forecast, yesterday_forecast, int(yesterday))
    
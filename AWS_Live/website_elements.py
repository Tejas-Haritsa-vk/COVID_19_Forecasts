import pandas as pd
import plotly.graph_objects as go

def embbed_graph(region):
    updatemenus = list([    dict(active=0, buttons=list([
                dict(label = 'Total',
                     method = 'update',
                     args = [{'visible': [True, True, True, True, True, True, True, False, False, False, False]},
                             {'title': 'COVID-19 Cases Forecast - Total Cases',
                              'annotations': ''}]),
                dict(label = 'Daywise',
                     method = 'update',
                     args = [{'visible': [False, False, False, False, False, False, False, True, True, True, True]},
                             {'title': 'COVID-19 Cases Forecast - New Cases',
                              'annotations': ''}]),        ]),
                x = 0.01,
                xanchor = 'left',
                y = 1.03,
                yanchor = 'top',    )  ])

    df = pd.read_csv("COVID_Database.csv")
    states_df = df.groupby('Region')
    df = pd.read_csv("COVID_Forecasted.csv")
    states_df2 = df.groupby('Region')
    #Create the graph
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=pd.DataFrame(states_df2.get_group(region))["Date"], y=pd.DataFrame(states_df.get_group(region))["Confirmed_Cases"], mode='lines+markers', name='Confirmed Cases'))
    fig.add_trace(go.Scatter(x=pd.DataFrame(states_df2.get_group(region))["Date"], y=pd.DataFrame(states_df.get_group(region))["Active_Cases"], mode='lines', name='Active Cases'))
    fig.add_trace(go.Scatter(x=pd.DataFrame(states_df2.get_group(region))["Date"], y=pd.DataFrame(states_df.get_group(region))["Cured/Discharged"], mode='lines', name='Cured/Discharged'))
    fig.add_trace(go.Scatter(x=pd.DataFrame(states_df2.get_group(region))["Date"], y=pd.DataFrame(states_df.get_group(region))["Death"], mode='lines', name='Deaths'))
    fig.add_trace(go.Scatter(x=pd.DataFrame(states_df2.get_group(region))["Date"], y=pd.DataFrame(states_df2.get_group(region))["Forecasted"], mode='lines+markers', name='Forecasted Cases', line=dict(color='rgb(255, 100, 50)'), legendgroup="Forecasts"))
    fig.add_trace(go.Scatter(x=pd.DataFrame(states_df2.get_group(region))["Date"], y=pd.DataFrame(states_df2.get_group(region))["Forecasted_high"], mode='lines', name='Forecasted Cases', fill=None, line=dict(color='rgb(255, 150, 50)'), legendgroup="Forecasts", showlegend=False))
    fig.add_trace(go.Scatter(x=pd.DataFrame(states_df2.get_group(region))["Date"], y=pd.DataFrame(states_df2.get_group(region))["Forecasted_low"], mode='lines', name='Forecasted Cases', line=dict(color='rgb(255, 150, 50)'), fill='tonexty', legendgroup="Forecasts", showlegend=False))


    fig.add_trace(go.Scatter(x=pd.DataFrame(states_df2.get_group(region))["Date"], y=pd.DataFrame(states_df2.get_group(region))["Confirmed_Cases_Daywise"], mode='lines+markers', name='Confirmed Cases', visible=False))
    fig.add_trace(go.Scatter(x=pd.DataFrame(states_df2.get_group(region))["Date"], y=pd.DataFrame(states_df2.get_group(region))["Forecasted_Cases_Daywise"], mode='lines+markers', name='Forecasted Cases', line=dict(color='rgb(255, 100, 50)'), legendgroup="Forecasts", visible=False))
    fig.add_trace(go.Scatter(x=pd.DataFrame(states_df2.get_group(region))["Date"], y=pd.DataFrame(states_df2.get_group(region))["Forecasted_Cases_high_Daywise"], mode='lines', name='Forecasted Cases', fill=None, line=dict(color='rgb(255, 150, 50)'), legendgroup="Forecasts", showlegend=False, visible=False))
    fig.add_trace(go.Scatter(x=pd.DataFrame(states_df2.get_group(region))["Date"], y=pd.DataFrame(states_df2.get_group(region))["Forecasted_Cases_low_Daywise"], mode='lines', name='Forecasted Cases', line=dict(color='rgb(255, 150, 50)'), fill='tonexty', legendgroup="Forecasts", showlegend=False, visible=False))

    #fig.update_xaxes(tickangle=45, tickformat = '%d-%m')

    #Edit the layout
    fig.update_layout(template='plotly_white', legend=dict(x=0.01, y=0.95), margin=dict(l=20, r=20, t=50, b=20), hovermode='x unified', updatemenus=updatemenus)
    fig.update_layout(title='COVID-19 Cases Forecast - Total Cases', xaxis_title='Date', yaxis_title='Number of Cases')
    # fig.show()
    
    go_fig = fig.to_html(full_html=False)
    
    return go_fig


def get_menu():
    return '''<head>
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
</head>
<body>

<div class="header">
  <h1 class="Title" style="font:Times New Roman; padding: 20px 0px 0px 0px; color: white;"> COVID-19 Forecasts </h1>
  <div class="navbar">
  <a href="http://127.0.0.1:5000/Home">Home</a>
  <a href="">News</a>
  <div class="dropdown">
    <button class="dropbtn">States 
      <i class="fa fa-caret-down"></i>
    </button>
    <div class="dropdown-content">
      <a href="http://127.0.0.1:5000/forecast?region=Karnataka">Karnataka</a>
      <a href="http://127.0.0.1:5000/forecast?region=Goa">Goa</a>
      <a href="http://127.0.0.1:5000/forecast?region=Telangana">Telangana</a>
    </div>
  </div> 
  </div>
</div>

</body>'''


def add_cases_compare(region, yesterday):
    df = pd.read_csv("Forecast.csv")
    yesterday_forecast = int(df[df.Region==region].iloc[0,-1])
    return '''<p style="font:Helvetica; color:#fff;  position: absolute;  right: 10px;  top: 60px;  z-index: 1; text-align:right; line-height: 1.5;"> Our Forcasted Cases Yesterday: <strong style="font-size: 18px;">{}</strong> <br> Confirmed Cases Yesterday: <strong style="font-size: 16px;">{}</strong></p>'''.format(yesterday_forecast, yesterday)

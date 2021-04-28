import requests
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy 
from bs4 import BeautifulSoup

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():

    url_days = 'http://dataservice.accuweather.com/forecasts/v1/daily/5day/222191'
    url_hours = 'http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/222191'
    weather_data_days = []
    weather_data_hours = []

    r_days = requests.get(url_days, 
        params={
            'apikey': 'BxUaMxMuWk7wRKPstIlDJktFyMgjGgeq'
        }).json()
    r_hours = requests.get(url_hours, 
        params={
            'apikey': 'BxUaMxMuWk7wRKPstIlDJktFyMgjGgeq'
        }).json()

    for i in range(5):

        weather = {
            'date': r_days['DailyForecasts'][i]['Date'],
            'min_temp': int(r_days['DailyForecasts'][i]['Temperature']['Minimum']['Value'] - 32),
            'max_temp': int(r_days['DailyForecasts'][i]['Temperature']['Maximum']['Value'] - 32),
            'day': r_days['DailyForecasts'][i]['Day']['IconPhrase'],
            'day_prec': r_days['DailyForecasts'][i]['Day']['HasPrecipitation'],
            'night': r_days['DailyForecasts'][i]['Night']['IconPhrase'],
            'night_prec': r_days['DailyForecasts'][i]['Night']['HasPrecipitation'],
        }

        weather_data_days.append(weather)

    for i in range(12):

        weather = {
            'datetime': r_hours[i]['DateTime'],
            'temp': int(r_hours[i]['Temperature']['Value'] - 32),
            'desc': r_hours[i]['IconPhrase'],
            'prec': r_hours[i]['HasPrecipitation'],
            'daylight': r_hours[i]['IsDaylight'],
            'prec_prob': r_hours[i]['PrecipitationProbability']
        }

        weather_data_hours.append(weather)

    return render_template('weather.html', weather_data_days=weather_data_days,  weather_data_hours=weather_data_hours)


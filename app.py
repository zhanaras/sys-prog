import requests
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy 
from bs4 import BeautifulSoup

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET'])
def form():
    return render_template('search.html')


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        new_city = request.form['city']
        
        url_city = 'http://dataservice.accuweather.com/locations/v1/cities/search'
        url_days = 'http://dataservice.accuweather.com/forecasts/v1/daily/5day/{}'
        url_hours = 'http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/{}'
        api_key = '8y059JI2OoAmDhmkFBb8DAGEFMAJDGFS'
        weather_data_days = []
        weather_data_hours = []

        r_city_key = requests.get(url_city, 
            params={
                'apikey': api_key,
                'q' : new_city
            }).json()

        city = {
            'name': r_city_key[0]['LocalizedName'],
            'city_key': r_city_key[0]['Key'],
            'country': r_city_key[0]['Country']['LocalizedName']
        }

        r_days = requests.get(url_days.format(city['city_key']), 
            params={
                'apikey': api_key,
                'details': 'true'
            }).json()
        r_hours = requests.get(url_hours.format(city['city_key']), 
            params={
                'apikey': api_key,
                'details': 'true'
            }).json()

        weather_desc = r_days['Headline']['Text']
    
        for i in range(5):

            weather = {
                'date': r_days['DailyForecasts'][i]['Date'],
                'min_temp': int(r_days['DailyForecasts'][i]['Temperature']['Minimum']['Value'] - 32),
                'max_temp': int(r_days['DailyForecasts'][i]['Temperature']['Maximum']['Value'] - 32),
                'feels_like': int(((int(r_days['DailyForecasts'][i]['RealFeelTemperature']['Maximum']['Value'])+int(r_days['DailyForecasts'][i]['RealFeelTemperature']['Minimum']['Value']))/2)-32),
                'day': r_days['DailyForecasts'][i]['Day']['ShortPhrase'],
                'night': r_days['DailyForecasts'][i]['Night']['ShortPhrase'],
            }

            weather_data_days.append(weather)

        for i in range(12):

            weather = {
                'datetime': r_hours[i]['DateTime'],
                'temp': int(r_hours[i]['Temperature']['Value'] - 32),
                'feels_like': int(r_hours[i]['RealFeelTemperature']['Value'] - 32),
                'uv': r_hours[i]['UVIndex'],
                'uv_text': r_hours[i]['UVIndexText'],
                'humidity': r_hours[i]['RelativeHumidity'],
                'wind_speed': r_hours[i]['Wind']['Speed']['Value'],
                'wind_speed_unit': r_hours[i]['Wind']['Speed']['Unit'],
                'desc': r_hours[i]['IconPhrase'],
                'prec': r_hours[i]['HasPrecipitation'],
                'daylight': r_hours[i]['IsDaylight'],
                'prec_prob': r_hours[i]['PrecipitationProbability']
            }

            weather_data_hours.append(weather)

        return render_template('weather.html', weather_data_days=weather_data_days,  weather_data_hours=weather_data_hours, city=city, weather_desc=weather_desc)


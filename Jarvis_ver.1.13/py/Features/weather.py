from talk import talk
talk('one moment')
from talk import *
from if_online import *
import requests
from datetime import datetime
import pytz
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
import timezonefinder
engine.setProperty("rate", 150)

if online:
    global temperature, humidity, type_of_temperature
    url = str(
        "https://api.openweathermap.org/data/2.5/weather?q=Lahore&appid=d4be8e123adba5a49a451c7bd54e558b")
    city_name = "Lahore"
    geolocator = Nominatim(user_agent='geoapiExercises')
    location = geolocator.geocode(city_name)
    initial = TimezoneFinder()
    result = initial.timezone_at(lng=location.longitude, lat=location.latitude)
    get_time = pytz.timezone(result)
    local_time = datetime.now(get_time)
    time = local_time.strftime('%I:%M %p')
    weather_data = requests.get(url).json()
    condition = weather_data['weather'][0]['main']
    description = weather_data['weather'][0]['description']
    temperature = int(weather_data['main']['temp'] - 273.15)
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']

    print('Temperature: ' + str(temperature) + '°\nWind: ' + str(wind_speed) + '\nHumidity: ' + str(
        humidity) + '%\nDescription: ' + condition + '\n\nLocal Time at ' + city_name + ': ' + time)
    talk('In lahore, It is ' + str(temperature) + 'degrees Celsius. The weather feels ' + condition + 'and humidity is ' +
         str(humidity) + 'percent')
    engine.setProperty("rate", 180)
else:
    print("Internet is not available. Try again later.")
    talk("Internet is not available. Try again later.")
    engine.setProperty("rate", 180)

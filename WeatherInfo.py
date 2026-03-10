import requests

from pprint import pprint

API_KEY = 'Inter your api key'

city = input('Enter city name: ')

base_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

weather_data = requests.get(base_url).json()
weather_data = requests.get(base_url)

if weather_data.status_code == 200:
    pprint(weather_data.json())
else:
    print(f"Error {weather_data.status_code}: {weather_data.json().get('message')}")

pprint(weather_data)
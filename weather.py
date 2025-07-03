import requests
import os

os.system('cls')

url = 'http://api.weatherapi.com/v1/current.json?key=522203bf9db445f4aff122142250107&q=Lagos&aqi=no'

response = requests.get(url)
weather_json = response.json()

current = weather_json.get('current').get('temp_c')


print(current)
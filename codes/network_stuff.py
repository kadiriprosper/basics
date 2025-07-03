from calculator import calculate_area_of_circle

import requests
import os

os.system('cls')

print(calculate_area_of_circle(10, 20))

print('Loading the data')
repsonse = requests.get('http://api.open-notify.org/astros.json')

json = repsonse.json()
# print(json)

print('The people currently in space are:')
for name in json['people']:
    print(name['name'])
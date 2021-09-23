from pprint import pprint

import requests
import json

params = {
    'results': 10
}
response = requests.get('https://randomuser.me/api/', params=params)
result = response.json()
result_list = []

for i in range(params['results']):
    result_list.append(result['results'][i]['name']['first'] + " " + result['results'][i]['name']['last'])

pprint.pp(result_list)

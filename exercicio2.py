import requests
from dotenv import load_dotenv
from datetime import datetime, timezone
import os

load_dotenv()
now = datetime.now(timezone.utc)

url = 'https://api.intra.42.fr'
token = os.getenv('access_token')
header = {
    "Authorization": f'Bearer {token}'
}

#1. Choose the campus by city
city = input('Insira a cidade do campus:')

#2. Get the campus ID
campus_endpoint = '/v2/campus'
filter_campus = {
    "filter[city]": city
}
campus_response = requests.get(url + campus_endpoint, headers=header, params=filter_campus)
if campus_response.status_code != 200:
    print('Desculpe, não encontrei o campus.')
    exit()
campus_data = campus_response.json()
campus_id = campus_data[0]['id']

#3. Get locations of the given campus
locations_endpoint = f'/v2/campus/{campus_id}/locations'
locations_response = requests.get(url + locations_endpoint, headers=header)
locations_data = locations_response.json()

#4. 
for cadete in locations_data:
    user = cadete['user']['login']
    login_time = datetime.fromisoformat(cadete['begin_at'].replace('Z', '+00:00'))
    if cadete['end_at'] is None:
        logout_time = now
    else:
        logout_time = datetime.fromisoformat(cadete['end_at'].replace('Z', '+00:00'))
    total_time = logout_time - login_time
    print(f'{user} | {cadete['begin_at']} | {cadete['end_at']} |{total_time}')
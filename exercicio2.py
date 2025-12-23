import requests
from dotenv import load_dotenv
from datetime import datetime, timezone
from constellations import constellations
import os

load_dotenv()
now = datetime.now(timezone.utc)

url = 'https://api.intra.42.fr'
token = os.getenv('access_token')
header = {
    "Authorization": f'Bearer {token}'
}
campus_id_rj = '28'

#1. Insert you 42 user/login
login_intra = input('Insira seu user/login da intra:')

#2. Get locations of the given campus
locations_endpoint = f'/v2/campus/{campus_id_rj}/locations'
locations_response = requests.get(url + locations_endpoint, headers=header)
locations_data = locations_response.json()

for cadete in locations_data:
    user = cadete['user']['login']
    login_time = datetime.fromisoformat(cadete['begin_at'].replace('Z', '+00:00'))
    if cadete['end_at'] is None:
        logout_time = now
    else:
        logout_time = datetime.fromisoformat(cadete['end_at'].replace('Z', '+00:00'))
    total_time = logout_time - login_time
    print(f'{user} | {cadete['begin_at']} | {cadete['end_at']} |{total_time}')
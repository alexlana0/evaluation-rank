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

#1. Insert you 42 user/login
print()
print('🌌 Bem-vindo ao Radar das Constelações 42 🌌\n')
user = input('Digite seu login da intra: ').strip()
print()

#2. Get locations of the given campus (id RJ = '28')
locations_endpoint = f'/v2/campus/28/locations'
locations_response = requests.get(url + locations_endpoint, headers=header)
locations_data = locations_response.json()

#3. Inversing the constellation dict for a faster reserch
constellations_by_login = {}

for constellation, members in constellations.items():
    for login in members:
        constellations_by_login[login] = constellation

user_constellation = constellations_by_login[user]
print('=' * 65)
print(f'Constelação: {user_constellation}')
print('=' * 65)
print('👀 Cadetes online agora no campus:')
print()

#4. Searching for cadets of the user constellation
members_online = 0
for cadete in locations_data:
    login = cadete['user']['login']
    if cadete['end_at'] is None:
        if login in constellations_by_login:
            if constellations_by_login[login] == user_constellation:
                members_online += 1
                cluster = cadete['host'].split('r')[0]
                if cluster == 'c1':
                    cluster = "mac's"
                else:
                    cluster = "dell's"
                print(f'🟢 {login:<10} | cluster dos {cluster:<6} | máquina {cadete["host"]}') 


print('\n' + '-' * 65)

if members_online == 0:
    print('😴 Nenhum cadete da sua constelação está no campus agora...')
elif members_online == 1:
    print('🔥 Tem 1 cadete da sua constelação resistindo no campus agora!')
else:
    print(f'🔥 Tem {members_online} cadetes da sua constelação no campus agora!')

print('-' * 65)
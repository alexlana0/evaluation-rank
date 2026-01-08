import requests
import json
from dotenv import load_dotenv
from datetime import datetime, timezone
from constellations import constellations
import os

load_dotenv()
now = datetime.now(timezone.utc)

url = 'https://api.intra.42.fr'
token = os.getenv('access_token')
webhook_url = os.getenv("DISCORD_WEBHOOK_URL")
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

#3. Inverting the constellation dictionary for faster search
constellations_by_login = {}

for constellation, members in constellations.items():
    for login in members:
        constellations_by_login[login] = constellation

user_constellation = constellations_by_login[user]
total_members = len(constellations[user_constellation])

#4. Searching for cadets in user constellation
lines = []
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
                lines.append(
                    f"🟢 **{login}** | cluster dos **{cluster}** | máquina `{cadete['host']}`"
                )

if members_online == 0:
    members_status = f"😴 0/{total_members} online"
    footer_text = 'Campus em silêncio… ninguém da constelação no campus agora.'
elif members_online == 1:
    members_status = f"👤 1/{total_members} online"
    footer_text = 'Um guerreiro solitário segurando o campus.'
elif members_online == total_members:
    members_status = f"🔥 {members_online}/{total_members} online"
    footer_text = 'Constelação completa! Todo mundo marcou presença hoje.'
else:
    members_status = f"👥 {members_online}/{total_members} online"
    footer_text = 'Sua constelação está marcando território no campus.'

payload = {
    "embeds": [
        {
            "title": "🌌 Radar das Constelações 42",
            "description": "\n".join(lines) if lines else "—",
            "color": 0x5B8CFF,
            "fields": [
                {
                    "name": "Constelação",
                    "value": f"**{user_constellation}**",
                    "inline": True
                },
                {
                    "name": "Membros",
                    "value": members_status,
                    "inline": True
                    }
            ],
            "footer": {
                "text": footer_text
            },
            "timestamp": now.isoformat()
        }
    ]
}

requests.post(
    webhook_url,
    data=json.dumps(payload),
    headers={"Content-Type": "application/json"}
)

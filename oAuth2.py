import requests
from dotenv import load_dotenv
import os

load_dotenv()

MY_AWESOME_UID = os.getenv('MY_AWESOME_UID')
MY_AWESOME_SECRET = os.getenv('MY_AWESOME_SECRET')

url = 'https://api.intra.42.fr/oauth/token'

query = {
    "grant_type": 'client_credentials',
    "client_id": MY_AWESOME_UID,
    "client_secret": MY_AWESOME_SECRET
}

response = requests.post(url, params=query)
data = response.json()
print(response)
print('Bearer token:')
print(data['access_token'])
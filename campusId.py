import requests
from dotenv import load_dotenv
import os

load_dotenv()

url = 'https://api.intra.42.fr'
token = os.getenv('access_token')
header = {
    "Authorization": f'Bearer {token}'
}

#1. Choose the campus by city
city = input('Insira a cidade:')

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
print(campus_id)
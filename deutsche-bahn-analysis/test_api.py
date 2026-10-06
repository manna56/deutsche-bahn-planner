import os
import requests
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv("DB_CLIENT_ID")
api_key = os.getenv("DB_API_KEY")

headers = {
    "DB-Client-ID": client_id,
    "DB-Api-Key": api_key
}

url = "https://apis.deutschebahn.com/db-api-marketplace/apis/timetables/v1/station/Berlin"

response = requests.get(url, headers=headers)

print("Status code:", response.status_code)
print("Response:")
print(response.text[:2000])
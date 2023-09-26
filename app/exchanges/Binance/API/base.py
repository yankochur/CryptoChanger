import requests
from decouple import config
import hmac
import hashlib
import time


API_KEY = config("API_KEY")
SECRET_KEY = config("API_SECRET")

url = 'https://api.binance.com/api/v3/account'

params = {
    'timestamp': int(time.time() * 1000),
}

query_string = '&'.join([f'{key}={params[key]}' for key in params])
signature = hmac.new(SECRET_KEY.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()

params['signature'] = signature

headers = {
    'X-MBX-APIKEY': API_KEY
}

response = requests.get(url, params=params, headers=headers)

if response.status_code == 200:
    account_data = response.json()

    for asset in account_data['balances']:
        if float(asset['free']) > 0:
            print(f"Asset: {asset['asset']}, Free: {asset['free']}, Locked: {asset['locked']}")
else:
    print(f"Error: {response.status_code}, {response.text}")

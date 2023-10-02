from decouple import config
from app.exchanges.Binance.lib.utils import get_timestamp
import hashlib
import hmac
import requests


class API(object):
    def __init__(self,
                 api_key=config("API_KEY"),
                 api_secret=config("API_SECRET"),
                 base_url='https://api.binance.com/api/v3/account',
                 headers=None,
                 params=None,
                 ):
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = base_url
        self.headers = {"X-MBX-APIKEY": api_key}
        self.params = None

    def hmac_connection(self):
        self.params = {"timestamp": get_timestamp()}

        query_string = '&'.join([f'{key}={self.params[key]}' for key in self.params])
        signature = hmac.new(self.api_secret.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()
        self.params['signature'] = signature

        response = requests.get(self.base_url, params=self.params, headers=self.headers)

        if response.status_code == 200:
            account_data = response.json()

            for asset in account_data['balances']:
                if float(asset['free']) > 0:
                    print(f"Asset: {asset['asset']}, Free: {asset['free']}, Locked: {asset['locked']}")
        else:
            print(f"Error: {response.status_code}, {response.text}")

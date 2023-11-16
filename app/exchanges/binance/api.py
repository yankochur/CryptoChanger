from decouple import config
from app.exchanges.api_lib.api_utils import get_timestamp, BaseAPI
import hashlib
import hmac
import requests


class BinanceAPI(BaseAPI):
    def __init__(self,
                 api_key=config("BINANCE_API_KEY"),
                 api_secret=config("BINANCE_API_SECRET"),
                 url="https://api.binance.com/api/v3/account",
                 headers=None,
                 params=None,
                 ):
        self.api_key = api_key
        self.api_secret = api_secret
        self.url = url
        self.headers = {"X-MBX-APIKEY": api_key}
        self.params = None

    def hmac_connection(self):
        self.params = {"timestamp": get_timestamp()}

        query_string = "&".join([f"{key}={self.params[key]}" for key in self.params])
        signature = hmac.new(self.api_secret.encode("utf-8"), query_string.encode("utf-8"), hashlib.sha256).hexdigest()
        self.params["signature"] = signature

        response = requests.get(self.url, params=self.params, headers=self.headers)

        if response.status_code == 200:
            account_data = response.json()

            # print("binance Balance:")

            balance_result = []

            for asset in account_data['balances']:
                if float(asset['free']) > 0:
                    balance_result.append(asset)
                    # print(f"Asset: {asset['asset']}, Free: {asset['free']}, Locked: {asset['locked']}")
            return balance_result
        else:
            return f"Error: {response.status_code}, {response.text}"
            # print(f"Error: {response.status_code}, {response.text}")

from decouple import config
from app.exchanges.lib.utils import get_timestamp
from urllib.parse import urlencode
import requests
import hashlib
import hmac


class API(object):
    def __init__(self,
                 api_key=config("BYBIT_API_KEY"),
                 api_secret=config("BYBIT_API_SECRET"),
                 url='https://api.bybit.com/v5/account/wallet-balance',
                 ):
        self.api_key = api_key
        self.api_secret = api_secret
        self.recv_window = str(5000)
        self.url = url
        self.headers = {
            "X-BAPI-API-KEY": api_key,
            "X-BAPI-TIMESTAMP": str(get_timestamp()),
            "X-BAPI-RECV-WINDOW": self.recv_window,
            "Content-Type": "application/json"
        }
        self.params = {
            "accountType": "SPOT",
            "coin": "USDT",
        }

    def hmac_connection(self):
        query_string = urlencode(self.params)

        param_str = str(get_timestamp()) + self.api_key + self.recv_window + query_string
        signature = hmac.new(bytes(self.api_secret, "utf-8"), param_str.encode("utf-8"), hashlib.sha256).hexdigest()
        self.headers["X-BAPI-SIGN"] = signature

        response = requests.get(self.url, params=self.params, headers=self.headers)

        if response.status_code == 200:
            print(response.text)

        else:
            print(f"Error: {response.status_code}, {response.text}")

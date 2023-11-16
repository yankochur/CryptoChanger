from decouple import config
from app.exchanges.api_lib.api_utils import BaseAPI
import datetime
import hmac
import base64
import requests


class OkxAPI(BaseAPI):
    def __init__(self,
                 api_key=config("OKX_API_KEY"),
                 api_secret=config("OKX_API_SECRET"),
                 api_passphrase=config("OKX_PASSPHRASE"),
                 url="https://www.okx.com",
                 ):
        self.api_key = api_key
        self.api_secret = api_secret
        self.api_passphrase = api_passphrase
        self.base_url = url

    def create_signature(self, timestamp, method, request_path, body=''):
        if str(body) == '{}' or str(body) == 'None':
            body = ''
        message = str(timestamp) + str.upper(method) + request_path + str(body)
        signature = hmac.new(bytes(self.api_secret, encoding='utf8'), bytes(message, encoding='utf8'), digestmod='sha256').digest()
        return base64.b64encode(signature)

    def get_time(self):
        now = datetime.datetime.utcnow()
        t = now.isoformat("T", "milliseconds")
        timestamp = t + "Z"
        return timestamp

    def get_balance(self):
        timestamp = self.get_time()
        method = "GET"
        endpoint = "/api/v5/account/balance"
        url = self.base_url + endpoint
        headers = {
            "OK-ACCESS-KEY": self.api_key,
            "OK-ACCESS-PASSPHRASE": self.api_passphrase,
            "OK-ACCESS-TIMESTAMP": timestamp,
            "OK-ACCESS-SIGN": self.create_signature(timestamp, method, endpoint)
        }

        response = requests.get(url, headers=headers).json()
        # print("OKX balance:")

        balance = response["data"][0]["details"]
        # print(balance)
        return balance

import urllib3
from decouple import config
from app.exchanges.api_lib.api_utils import get_timestamp, BaseAPI
from urllib.parse import urlencode, quote_plus
import requests
import hashlib
import hmac


class ByBitAPI(BaseAPI):
    def __init__(self,
                 api_key=config("BYBIT_API_KEY"),
                 api_secret=config("BYBIT_API_SECRET"),
                 url= "https://api.bybit.com/spot/v3/private/account",
                 ):
        self.api_key = api_key
        self.api_secret = api_secret
        self.recv_window = str(5000)
        self.url = url
        self.headers = {
            "X-BAPI-API-KEY": api_key,
            "X-BAPI-TIMESTAMP": str(get_timestamp()),
            "X-BAPI-RECV-WINDOW": self.recv_window,
        }
        # self.params = {
        #     "accountType": "SPOT",
        #     "coin": "USDT",
        # }
        self.params = {
            "api_key": api_key,
            "timestamp": round(get_timestamp()),
            "recv_window": 10000
        }

    def hmac_connection(self):
        # query_string = urlencode(self.params)
        #
        # param_str = str(get_timestamp()) + self.api_key + self.recv_window + query_string
        # signature = hmac.new(bytes(self.api_secret, "utf-8"), param_str.encode("utf-8"), hashlib.sha256).hexdigest()
        # self.headers["X-BAPI-SIGN"] = signature
        #
        # response = requests.get(self.url+"?"+query_string, headers=self.headers)
        #
        # print(param_str)
        # print(query_string)
        # print(self.params)
        # print(self.headers)
        #
        # if response.status_code == 200:
        #     print(response.text)
        #
        # else:
        #     print(f"Error: {response.status_code}, {response.text}")

        param_str = urlencode(
            sorted(self.params.items(), key=lambda tup: tup[0])
        )

        signature_hash = hmac.new(
            bytes(self.api_secret, "utf-8"),
            param_str.encode("utf-8"),
            hashlib.sha256
        )

        signature = signature_hash.hexdigest()
        sign_real = {
            "sign": signature
        }

        param_str = quote_plus(param_str, safe="=&")
        full_param_str = f"{param_str}&sign={sign_real['sign']}"

        headers = {"Content-Type": "application/json"}

        urllib3.disable_warnings()

        response = requests.get(f"{self.url}?{full_param_str}", headers=headers, verify=False).json()
        # print("bybit Balance:")

        balances = response.get("result")["balances"]
        # print(balances)
        return balances

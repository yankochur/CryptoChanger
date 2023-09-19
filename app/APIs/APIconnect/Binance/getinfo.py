from app.APIs.APIconnect.base import BaseExchangesAPI
import requests


class BinanceAPI(BaseExchangesAPI):
    BASE_URL = 'https://api.binance.com/api/v3'

    def get_account_info(self):
        endpoint = 'account'
        headers = {'X-MBX-APIKEY': self.api_key}
        response = requests.get(f"{self.BASE_URL}{endpoint}", headers=headers)
        return response.json()

    def place_order(self, symbol, price, quantity, side, order_type):
        endpoint = 'order'
        headers = {'X-MBX-APIKEY': self.api_key}
        params = {
            'symbol': symbol,
            'price': price,
            'quantity': quantity,
            'side': side,
            'type': order_type,
        }
        response = requests.post(f"{self.BASE_URL}{endpoint}", headers=headers)
        return response.json()

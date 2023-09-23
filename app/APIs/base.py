
class BaseExchangesAPI:
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret

    def get_account_info(self):
        raise NotImplementedError("Subclasses must implement get_account_info method")

    def place_order(self, symbol, price, quantity, side, order_type):
        raise NotImplementedError("Subclasses must implement place_order method")

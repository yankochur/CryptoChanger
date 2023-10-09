# from app.__init__ import create_app
from app.exchanges.binance import api as binance_api
from app.exchanges.bybit import api as bybit_api


BINANCE_CONNECTION = binance_api.BinanceAPI()
BYBIT_CONNECTION = bybit_api.ByBitAPI()


if __name__ == '__main__':
    BINANCE_CONNECTION.hmac_connection()
    BYBIT_CONNECTION.hmac_connection()

# from app.__init__ import create_app
from app.exchanges.Binance import api as binance_api
from app.exchanges.ByBit import api as bybit_api


BINANCE_CONNECTION = binance_api.API()
BYBIT_CONNECTION = bybit_api.API()


if __name__ == '__main__':
    BINANCE_CONNECTION.hmac_connection()
    BYBIT_CONNECTION.hmac_connection()

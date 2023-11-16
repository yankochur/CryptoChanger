from app.flaskapp import create_app
from app.exchanges.binance import api as binance_api
from app.exchanges.bybit import api as bybit_api
from app.exchanges.okx import api as okx_api

BINANCE_CONNECTION = binance_api.BinanceAPI()
BYBIT_CONNECTION = bybit_api.ByBitAPI()
OKX_CONNECTION = okx_api.OkxAPI()


if __name__ == '__main__':
    # BINANCE_CONNECTION.hmac_connection()
    # BYBIT_CONNECTION.hmac_connection()
    # OKX_CONNECTION.get_balance()
    create_app().run(debug=True)

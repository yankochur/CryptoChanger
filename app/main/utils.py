from app.exchanges.binance import api as binance_api
from app.exchanges.bybit import api as bybit_api
from app.exchanges.okx import api as okx_api


def get_balances():
    binance_connection = binance_api.BinanceAPI()
    bybit_connection = bybit_api.ByBitAPI()
    okx_connection = okx_api.OkxAPI()

    binance = binance_connection.hmac_connection()
    bybit = bybit_connection.hmac_connection()
    okx = okx_connection.get_balance()

    data = {
        "binance_api": binance,
        "bybit_api": bybit,
        "okx_api": okx,
    }

    return data
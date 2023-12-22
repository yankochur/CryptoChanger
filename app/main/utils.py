from app.exchanges.binance import api as binance_api
from app.exchanges.bybit import api as bybit_api
from app.exchanges.okx import api as okx_api

from passlib.context import CryptContext


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


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hasher:
    @staticmethod
    def verify_password(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def get_password_hash(password):
        return pwd_context.hash(password)

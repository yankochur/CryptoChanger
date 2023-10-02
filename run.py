# from app.__init__ import create_app
from app.exchanges.Binance import api

connection = api.API()

if __name__ == '__main__':
    connection.hmac_connection()

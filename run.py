# from app.__init__ import create_app
from app.exchanges.Binance import api

connection = api.API()

if __name__ == '__main__':
    # create_app().run(debug=True)
    # base.ws.run_forever()
    # base.binance_balance()
    connection.hmac_connection()

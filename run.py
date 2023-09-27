# from app.__init__ import create_app
from app.exchanges.Binance.lib import base

if __name__ == '__main__':
    # create_app().run(debug=True)
    # base.ws.run_forever()
    # base.binance_balance()
    print(base.account_data)

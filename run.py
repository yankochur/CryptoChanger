# from app.__init__ import create_app
from app.get_info.wallet_binance import get_account_info_binance

if __name__ == '__main__':
    # create_app().run(debug=True)
    get_account_info_binance()

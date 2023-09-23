from app.APIs.Binance.getinfo import BinanceAPI


def get_account_info_binance():

    binance = BinanceAPI(api_key, api_secret)

    account_info = binance.get_account_info()

    print("Информация об аккаунте:")
    print(account_info)
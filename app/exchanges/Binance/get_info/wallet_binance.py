from app.exchanges.Binance.getinfo import BinanceAPI


def get_account_info_binance():
    api_key = 'QWCQIukvYvBdtjmZWT6FDaE5hKlb6eth58zO39AXPA6xqSSlPztyYYhhhzyZTB12'
    api_secret = 'vkOJGdIdhyxMCfcsVxoMIq3d8j2vyEu3gQSH12ReYQByhfnGg1yIW3mYzOLt2G6x'

    binance = BinanceAPI(api_key, api_secret)

    account_info = binance.get_account_info()

    print("Информация об аккаунте:")
    print(account_info)
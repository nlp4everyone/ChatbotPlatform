import requests
from config import params
class CoingeckoAPI():
    @staticmethod
    def get_currency_information(currency_url=params.current_price_url):
        json = requests.get(currency_url)

    @staticmethod
    def get_market_history(history_url=params.history_crypto_url):
        response = requests.get(history_url)
        if response.status_code != 200:
            return None
        return response.json()
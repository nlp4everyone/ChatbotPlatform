import requests
from config import params
from enum import Enum
coingecko_url = "https://pro-api.coingecko.com/api/v3/"
coingecko_key = params.coingecko_key
token_ids = params.token_ids

class PeriodType(Enum):
    HOURLY = 0
    DAILY = 1

class CoingeckoAPI():
    @staticmethod
    def get_currency_information(currency_url):
        json = requests.get(currency_url)

    @staticmethod
    def get_market_history(days=7,period_type=PeriodType.DAILY):
        period = 'hourly'
        # Check period
        if period_type == PeriodType.DAILY:
            period = "daily"
            market_url = coingecko_url + f"coins/{token_ids}/market_chart?vs_currency=usd&days={days}&interval={period}&x_cg_pro_api_key={coingecko_key}"
        else:
            market_url = coingecko_url + f"coins/{token_ids}/market_chart?vs_currency=usd&days={days}&x_cg_pro_api_key={coingecko_key}"
        # Define url


        # Get state
        response = requests.get(market_url)
        # Return value
        if response.status_code != 200:
            raise Exception("Wrong data")
        return response.json()
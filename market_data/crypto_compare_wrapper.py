import market_data.market_data_wrapper
import requests
import json
from datetime import datetime as dt
import time


class CryptoCompareWrapper(market_data.market_data_wrapper.MarketDataWrapper):
    def __init__(self, rest_period=2):
        super().__init__()
        self._URL = 'https://min-api.cryptocompare.com/data/'
        self.last_call = dt.now()
        self.rest_period = rest_period

    def _make_api_call(self, params):
        self._wait()
        response = requests.get(self._URL + params)
        response.raise_for_status()

        return json.loads(response.text)

    def _wait(self):
        """
                This method prevents the REST api to be called to frequently
                :return: None
                """
        call_time = dt.now()
        while (call_time - self.last_call).seconds < self.rest_period:
            time.sleep(1)
            call_time = dt.now()

        self.last_call = call_time

    def get_all_historical_data_for_currency(self, pairs):
        """See https://min-api.cryptocompare.com/data/histoday?fsym=BTC&tsym=USD&limit=2000&allData for data example

        :param pairs: tuple object in the format of ("BTC", "USD") etc
        :return: json {"Response": "Success", "Type":100, "Aggregated" false, "Data":[{"...
        """
        params = 'histoday?fsym={}&tsym={}&limit=2000&allData'.format(pairs[0], pairs[1])
        return self._make_api_call(params)

    def get_all_historical_data_for_currency_from_today(self, pairs, days):
        """See https://min-api.cryptocompare.com/data/histoday?fsym=BTC&tsym=USD&limit=2000 for data example

        :param pairs: tuple object in the format of ("BTC", "USD") etc.
        :param days: for how many days back to fetch data.
        :return: json {"Response": "Success", "Type":100, "Aggregated" false, "Data":[{"...
        """
        params = 'histoday?fsym={}&tsym={}&limit={}'.format(pairs[0], pairs[1], days)
        return self._make_api_call(params)

    def get_hourly_data_for_currency(self, pairs, hours=24):
        """See https://min-api.cryptocompare.com/data/histohour?fsym=BTC&tsym=USD&limit=2000for data example

                :param pairs: tuple object in the format of ("BTC", "USD") etc.
                :param hours: amount of hours to return.
                :return: json {"Response": "Success", "Type":100, "Aggregated" false, "Data":[{"...
                """
        params = 'histohour?fsym={}&tsym={}&limit={}'.format(pairs[0], pairs[1], hours)
        return self._make_api_call(params)

    def get_minute_data_for_currency(self, pairs, minutes):
        """See https://min-api.cryptocompare.com/data/histominute?fsym=BTC&tsym=USD&limit=2000for data example

                        :param pairs: tuple object in the format of ("BTC", "USD") etc.
                        :param minutes: amount of minutes to return.
                        :return: json {"Response": "Success", "Type":100, "Aggregated" false, "Data":[{"...
                        """
        params = 'histominute?fsym={}&tsym={}&limit={}'.format(pairs[0], pairs[1], minutes)
        return self._make_api_call(params)

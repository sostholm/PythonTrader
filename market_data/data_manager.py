from datetime import datetime as dt
import pandas as pd
from market_data.crypto_compare_wrapper import CryptoCompareWrapper
import logging


class DataManager(object):

    def __init__(self, top_list=10):
        self.logger = logging.getLogger('DataManager')
        hdlr = logging.FileHandler('logs\DataManager.log')
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        hdlr.setFormatter(formatter)
        self.logger.addHandler(hdlr)
        self.logger.setLevel(logging.DEBUG)

        self.market_data = pd.DataFrame(index=['currency', 'date'])
        self.top_list = top_list
        self.crypto_compare = CryptoCompareWrapper()
        self._load()

    def _load(self):
        """
        Attempts to loads data from pickle or if absent download new data.
        :return: None
        """
        self.currency_list = self._load_top_list_crypto_compare()

        try:
            self.market_data = pd.read_pickle('data/market_data.pickle')
            self.logger.info('Successfully loaded market_data.pickle')
            self.update()
        except FileNotFoundError:
            self.logger.error('market_data.pickle not found')
            self._download_market_data()
        self._save()

    def _save(self):
        """
        Save data to pickle
        :return: None
        """
        self.market_data.to_pickle('data/market_data.pickle')
        self.logger.info('market_data.pickle successfully saved')

    def update(self):
        """
        Tests to see if the time delta between the last index of the data and now is greater than 1 day.
        If so, download the missing data.
        :return: Pandas DataFrame
        """
        last_date = self.market_data.index.max()[1]
        time_frame = (dt.now() - last_date).days

        if time_frame > 1:
            for currency in self.currency_list:
                new_data = self._load_specified_range_from_crypto_compare(currency=currency, days=time_frame)
                self.market_data = pd.concat([self.market_data, new_data])
        self.logger.info('market_data successfully updated')
        return self.market_data

    def _download_market_data(self):
        """Loads all data from crypto compare based on symbol"""

        dfs = []
        for currency in self.currency_list[0:self.top_list]:
            dfs.append(self._convert_data((currency, self._load_all_from_crypto_compare(currency))))

        self.logger.info('New market data downloaded')
        self.market_data = pd.concat(self._convert_data(dfs))

    def _convert_data(self, data):
        """
        Converts the unix timestamp to UTC dates and indexes this in combination with the currency sign
        :param data: JSON object returned from crypto sites coupled with currency name in a tuple
        :return: returns DataFrame
        """
        df = pd.DataFrame(data[1]['Data'])

        df['date'] = pd.to_datetime(df['time'], unit='s')
        df['currency'] = data[0]

        df.set_index(['currency', 'date'], inplace=True)

        return df

    def _load_all_from_crypto_compare(self, currency):
        """Loads the specified crypto from cryptocompare
            creates a mutli-index Dataframe"""
        data = self.crypto_compare.get_all_historical_data_for_currency((currency, 'USDT'))
        return self._convert_data(data, currency)

    def _load_specified_range_from_crypto_compare(self, days, currency, base='USDT', ):
        data = self.crypto_compare.get_all_historical_data_for_currency_from_today((currency, base), days)
        return self._convert_data((currency, data))

    def _load_top_list_crypto_compare(self):
        toplist = self.crypto_compare.get_currency_24h_volume_toplist(limit=self.top_list)
        return [currency['SYMBOL'] for currency in toplist['Data']]

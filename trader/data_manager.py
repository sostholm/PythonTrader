import requests
import json
from datetime import datetime as dt
import pandas as pd
import pickle
from bs4 import BeautifulSoup


class DataManager(object):

    def __init__(self):
        self.market_data = pd.DataFrame(index=['currency', 'date'])
        self.currency_list = pd.DataFrame()
        self.load()

    def load(self):
        try:
            self.market_data = pd.read_pickle('market_data.pickle')
        except FileNotFoundError:
            self._load_new_data()
            self._download_market_data()

    def update(self):
        last_date = self.market_data.index.max()[1]
        if (dt.now() - last_date).days > 1:
            pass

    def _get_historical_data_between(self, date, currency):
        pass

    def _download_market_data(self):
        """Loads 400 of the top crypto currency data"""

        dfs = []
        for x in range(400):
            dfs.append(self._load_from_cryptocompare(self.currency_list.iloc[x].symbol))

        self.market_data = pd.concat(dfs)

    def _load_from_cryptocompare(self, currency):
        """Loads the specified crypto from cryptocompare
            creates a mutli-index Dataframe"""

        url = 'https://min-api.cryptocompare.com/data/histoday?'
        params = 'fsym={}&tsym={}&limit=2000&e=CCCAGG&allData'.format(currency, 'BTC,USD')
        url = url + params
        history_data_json = requests.get(url)
        loaded = history_data_json.text

        df = pd.DataFrame(loaded['Data'])

        df['date'] = pd.to_datetime(df['time'], unit='s')
        df['currency'] = currency

        df.set_index(['currency', 'date'], inplace=True)

        return df

    def _load_new_data(self):
        """Checks if there is a pickle of coinmarketcap data if  not, load from website"""

        try:
            with open('coin_market_cap_data.pickle') as data:
                self.currency_list = pickle.load(data)
        except FileNotFoundError:
            market_cap_html = requests.get('https://coinmarketcap.com/all/views/all/')
            self.currency_list = self._parse_html_data(market_cap_html)

    def _parse_html_data(self, market_cap_html):
        """Processes the loaded data from coinmarket cap, yielding a dataframe"""

        soup = BeautifulSoup(market_cap_html.content, 'html.parser')
        tbody = soup.find('tbody')
        extracted_tbody = list(tbody.children)
        currencies = []

        for currency in extracted_tbody:
            if len(currency) > 1:
                try:
                    info = {}
                    info['name'] = currency.find('td', {'class': 'currency-name'}).find('a', {
                        'class': 'currency-name-container'}).text
                    info['symbol'] = currency.find('td', {'class': 'text-left col-symbol'}).text
                    info['market-cap_usd'] = currency.find('td', {'class': 'market-cap'})['data-usd']
                    info['price_usd'] = currency.find('a', {'class': 'price'})['data-usd']
                    try:
                        info['circulating-supply'] = currency.find('td', {'class': 'circulating-supply'}).find('a')[
                            'data-supply']
                    except:
                        info['circulating-supply'] = currency.find('td', {'class': 'circulating-supply'}).find('span')[
                            'data-supply']
                    info['volume_btc'] = currency.find('a', {'class': 'volume'})['data-btc']
                    info['volume_usd'] = currency.find('a', {'class': 'volume'})['data-usd']
                    currencies.append(info)
                except:
                    print('failed {}'.format(info))
                    print(currency)
        return pd.DataFrame(currencies)

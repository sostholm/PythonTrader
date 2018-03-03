import httplib2
import json
from urllib.parse import quote
import time
import hmac
import urllib
import requests
import hashlib
import base64
import sys

class CryptopiaUser(object):

    def __init__(self, API_KEY, API_SECRET):
        self.API_KEY = API_KEY
        self.API_SECRET = API_SECRET

        self.public = ['GetCurrencies', 'GetTradePairs', 'GetMarkets',
                       'GetMarket', 'GetMarketHistory', 'GetMarketOrders', 'GetMarketOrderGroups']
        self.private = ['GetBalance', 'GetDepositAddress', 'GetOpenOrders',
                        'GetTradeHistory', 'GetTransactions', 'SubmitTrade',
                        'CancelTrade', 'SubmitTip', 'SubmitWithdraw', 'SubmitTransfer']

    #Get market
    def getMarket(self):
        h = httplib2.Http(".cache")
        (resp_headers, content) = h.request("https://www.cryptopia.co.nz/api/GetMarket/CEFS_BTC", "GET")

        fcontent = json.loads(content)

        print(fcontent['Data']['LastPrice'])

    def secure_headers(url, post_data):
        nonce = str( int( time.time() ) )
        m = hashlib.md5()
        m.update(post_data.encode())
        requestContentBase64String = base64.b64encode(m.digest())
        signature = API_KEY + "POST" + urllib.parse.quote_plus( url ).lower() + nonce + requestContentBase64String.decode()
        hmacsignature = base64.b64encode(hmac.new(base64.b64decode( API_SECRET ), signature.encode(), hashlib.sha256).digest()).decode()
        header_value = "amx " + API_KEY + ":" + hmacsignature + ":" + nonce
        headers = { 'Authorization': header_value, 'Content-Type':'application/json; charset=utf-8' }
        return headers

    def api_query(self, request_param, get_param=None, post_param=None):
        if request_param in self.private:
            url = "https://www.cryptopia.co.nz/Api/" + request_param

            req = get_param

            post_data = json.dumps( req );
            headers = self.secure_headers(url, post_param)
            r = requests.post( url, data = post_data, headers = headers )

            response = r.text
            print("( Response ): " + response)

        elif request_param in self.public:
            url = "https://www.cryptopia.co.nz/Api/" + request_param + "/" + \
                  ('/'.join(i for i in get_parameters.values()) if get_param is not None else "")
            h = httplib2.Http(".cache")
            (resp_headers, content) = h.request(url, "GET")

            fcontent = json.loads(content)

            print(fcontent)

    def get_currencies(self):
        """ Gets all the currencies """
        return self.api_query(request_param='GetCurrencies')

    def get_tradepairs(self):
        """ GEts all the trade pairs """
        return self.api_query(request_param='GetTradePairs')

    def get_markets(self):
        """ Gets data for all markets """
        return self.api_query(request_param='GetMarkets')

    def get_market(self, market):
        """ Gets market data """
        return self.api_query(request_param='GetMarket',
                              get_parameters={'market': market})

    def get_history(self, market):
        """ Gets the full order history for the market (all users) """
        return self.api_query(request_param='GetMarketHistory',
                              get_parameters={'market': market})

    def get_orders(self, market):
        """ Gets the user history for the specified market """
        return self.api_query(request_param='GetMarketOrders',
                              get_parameters={'market': market})

    def get_ordergroups(self, markets):
        """ Gets the order groups for the specified market """
        return self.api_query(request_param='GetMarketOrderGroups',
                              get_parameters={'markets': markets})

    def get_balance(self, currency):
        """ Gets the balance of the user in the specified currency """
        result, error = self.api_query(request_param='GetBalance',
                                       post_param={'Currency': currency})
        if error is None:
            result = result[0]
        return (result, error)

    def get_openorders(self, market):
        """ Gets the open order for the user in the specified market """
        return self.api_query(request_param='GetOpenOrders',
                              post_param={'Market': market})

    def get_deposit_address(self, currency):
        """ Gets the deposit address for the specified currency """
        return self.api_query(request_param='GetDepositAddress',
                              post_param={'Currency': currency})

    def get_tradehistory(self, market):
        """ Gets the trade history for a market """
        return self.api_query(request_param='GetTradeHistory',
                              post_param={'Market': market})

    def get_transactions(self, transaction_type):
        """ Gets all transactions for a user """
        return self.api_query(request_param='GetTransactions',
                              post_param={'Type': transaction_type})

    def submit_trade(self, market, trade_type, rate, amount):
        """ Submits a trade """
        return self.api_query(request_param='SubmitTrade',
                              post_param={'Market': market,
                                               'Type': trade_type,
                                               'Rate': rate,
                                               'Amount': amount})

    def cancel_trade(self, trade_type, order_id, tradepair_id):
        """ Cancels an active trade """
        return self.api_query(request_param='CancelTrade',
                              post_param={'Type': trade_type,
                                               'OrderID': order_id,
                                               'TradePairID': tradepair_id})

    def submit_tip(self, currency, active_users, amount):
        """ Submits a tip """
        return self.api_query(request_param='SubmitTip',
                              post_param={'Currency': currency,
                                               'ActiveUsers': active_users,
                                               'Amount': amount})

    def submit_withdraw(self, currency, address, amount):
        """ Submits a withdraw request """
        return self.api_query(request_param='SubmitWithdraw',
                              post_param={'Currency': currency,
                                               'Address': address,
                                               'Amount': amount})

    def submit_transfer(self, currency, username, amount):
        """ Submits a transfer """
        return self.api_query(request_param='SubmitTransfer',
                              post_param={'Currency': currency,
                                               'Username': username,
                                               'Amount': amount})

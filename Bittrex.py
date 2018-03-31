import requests
import json
import time
import hmac
import hashlib

class Bittrex(object):

    def __init__(self, api_key='', api_secret=''):
        self.API_KEY = api_key
        self.API_SECRET = api_secret
    """
    ________________________________________________________________________________
    Core Methods--------------------------------------------------------------------
    ________________________________________________________________________________
    """

    def publicCall(self, request_param):
        request_url = "https://bittrex.com/api/v1.1/public/" + request_param['path']

        if 'market' in request_param:
            request_url += request_param['market']

        r = requests.get(request_url)
        accJson = json.loads(r.text)

        return accJson

    def privateCall(self, request_param):
        request_url = 'https://bittrex.com/api/v1.1/account/' + request_param['path'] + '?'
        nonce = str(int(time.time() * 1000))
        request_url = "{0}apikey={1}&nonce={2}&".format(request_url, self.API_KEY, nonce)

        if 'currency' in request_param:
            request_url += request_param['currency']

        apisign = self.apisign(request_url)
        r = requests.get(request_url, headers={'apisign': apisign})
        balance_json = json.loads(r.text)
        return balance_json


    def apisign(self, request_url):
        return hmac.new(self.API_SECRET.encode(), request_url.encode(), hashlib.sha512).hexdigest()

    """
    ________________________________________________________________________________
    End Core------------------------------------------------------------------------
    ________________________________________________________________________________
    """

    """
    ________________________________________________________________________________
    Public------------------------------------------------------------------------
    ________________________________________________________________________________
    """
    def getMarkets(self):
        request_param = {'path':'getmarkets'}
        return self.publicCall(request_param)

    def getTicker(self, market):
        request_param = {'path':'getticker?', 'market':'market=' + market}
        return self.publicCall(request_param)
    """
    ________________________________________________________________________________
    Private------------------------------------------------------------------------
    ________________________________________________________________________________
    """
    def getBalances(self):
        request_param = {'path':'getbalances'}
        return self.privateCall(request_param)

    def getBalance(self, currency):
        request_param = {'path':'getbalance', 'currency': '&currency=' + currency}
        return self.privateCall(request_param)

    def getOrderHistory(self, currency=''):
        if currency != '':
            request_param = {'path':'getorderhistory', 'currency': '&market=' + currency}
        else:
            request_param = {'path':'getorderhistory'}
        return self.privateCall(request_param)

    def getOrder(self, uuid):
        request_param = {'path':'getorder', 'currency': '&uuid=' + uuid}
        return self.privateCall(request_param)

    """
    ________________________________________________________________________________
    Market------------------------------------------------------------------------
    ________________________________________________________________________________
    """
    def buyLimit(self, market, quantity, rate):
        request_param = {'path':'buylimit', 'currency': 'market=' + market + '&quantity=' +quantity + '&rate=' + rate}
        return self.privateCall(request_param)

    def sellLimit(self, market, quantity, rate):
        request_param = {'path':'selllimit', 'currency': 'market=' + market + '&quantity=' +quantity + '&rate=' + rate}
        return self.privateCall(request_param)

    def cancelOrder(self, uuid):
        request_param = {'path':'cancel', 'currency': '&uuid=' + uuid}
        return self.privateCall(request_param)

    def getOpenOrders(self, market=''):
        if market == '':
            request_param = {'path':'getopenorders'}
        else:
            request_param = {'path':'getopenorders', 'currency': '&market=' + market}
        return self.privateCall(request_param)

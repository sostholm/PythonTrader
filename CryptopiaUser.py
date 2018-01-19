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

class CrypopiaUser(object):

    def __init__(self, API_KEY, API_SECRET):
        self.API_KEY = API_KEY
        self.API_SECRET = API_SECRET

        self.public = ['GetCurrencies', 'GetTradePairs', 'GetMarkets',
                       'GetMarket', 'GetMarketHistory', 'GetMarketOrders', 'GetMarketOrderGroups']
        self.private = ['GetBalance', 'GetDepositAddress', 'GetOpenOrders',
                        'GetTradeHistory', 'GetTransactions', 'SubmitTrade',
                        'CancelTrade', 'SubmitTip', 'SubmitWithdraw', 'SubmitTransfer']

    #Get market
    def getMarket():
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

    def getPrivate(self, request_param, get_param, post_param):
        if request_param in self.private
            url = "https://www.cryptopia.co.nz/Api/" + request_param
            #nonce = str( int( time.time() ) )

            #req = {'Currency':'BTC'}
            req = get_param

            post_data = json.dumps( req );
            #m = hashlib.md5()
            #m.update(post_data.encode())
            #requestContentBase64String = base64.b64encode(m.digest())
            #print(requestContentBase64String)
            #signature = API_KEY + "POST" + urllib.parse.quote_plus( url ).lower() + nonce + requestContentBase64String.decode()
            #hmacsignature = base64.b64encode(hmac.new(base64.b64decode( API_SECRET ), signature.encode(), hashlib.sha256).digest()).decode()
            #header_value = "amx " + API_KEY + ":" + hmacsignature + ":" + nonce
            #print(header_value)
            #headers = { 'Authorization': header_value, 'Content-Type':'application/json; charset=utf-8' }
            headers = self.secure_headers(url, post_param)
            r = requests.post( url, data = post_data, headers = headers )

            response = r.text
            print("( Response ): " + response)

        elif request_param in self.public:
            

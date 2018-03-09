import requests
import json
import time
import hmac
import hashlib

class Bittrex(object):

    def __init__(self, api_key='', api_secret=''):
        self.API_KEY = api_key
        self.API_SECRET = api_secret

    def apisign(self, request_url):
        return hmac.new(self.API_SECRET.encode(), request_url.encode(), hashlib.sha512).hexdigest()

    def getMarkets(self):
        r = requests.get("https://bittrex.com/api/v1.1/public/getmarkets")
        accJson = json.loads(r.text)

        return accJson

    def getBalance(self):
        request_url = 'https://bittrex.com/api/v1.1/account/getbalances?'
        nonce = str(int(time.time() * 1000))
        request_url = "{0}apikey={1}&nonce={2}&".format(request_url, self.API_KEY, nonce)
        apisign = self.apisign(request_url)
        r = requests.get(request_url, headers={'apisign': apisign})
        balance_json = json.loads(r.text)
        return balance_json

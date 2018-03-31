from CryptopiaUser import CryptopiaUser


API_KEY = 'f64f58cb2f1342068ba2689f049c2b9f'
API_SECRET = 'ssKtRB836MWX2sLmT4ZK9G5OL1N92WGfNxI45B4QKEQ='
API_KEY_BTRX = '8e12797de06c4fb9b4ba37c105a9e16b'
API_SECRET_BTRX = '6234a3267abb4c799258daf75defdd69'
API_KEY_hitBTC = '9aefce39ba2e12d97dfacc6369b0d993'
API_SECRET_hitBTC = '7d490d5091fd2c9a7f9ac99b9e17dbe4'

#crpUser = CryptopiaUser(API_KEY, API_SECRET)

#crpUser.getMarket()
#crpUser.get_currencies()

#from coinigy_socket import coinigy_socket
from CoinigyRest2 import CoinigyRest2
from Position import Position
from Bittrex import Bittrex
from hitBTC import hitBTC
from TraderHub import TraderHub
import multiprocessing as mp
from multiprocessing import Value
import pickle
import time
#coinigy = CoinigyRest2()
#coinigy_socket = coinigy_socket()
#coinigy_socket.start()
#json1 = coinigy.getBalance()
#json1 = json1['data']
"""
btc_price = coinigy.getBTCprice()
balanceJson = coinigy.getBalance()
json1 = balanceJson['data']
json2 = btc_price['data'][0]
balance = 0.0

for b in json1:
    balance += float(b['btc_balance'])
positions = []
for x in json1:
    positions.append(Position(x['balance_curr_code'], x['balance_amount_total']))
#print(balance)
print(balance)
print(float(json2['last_trade']) * balance)
print(positions)
coinigy.getAccounts()
"""
#btrx = Bittrex()
#

btrx = Bittrex(API_KEY_BTRX, API_SECRET_BTRX)
#print(btrx.getBalance())
#print(btrx.getMarkets())
#print(btrx.getTicker('BTC-XRP'))
#print(btrx.getTicker('BTC-LTC'))
#print(btrx.getBalance('XRP'))
#print(btrx.getOrderHistory('BTC-XRP'))


def multiBTRX(q, exchange, num):
    tr_hub = TraderHub(exchange, q, num)

if __name__ == '__main__':
    mp.set_start_method('spawn')
    q = mp.Queue()
    num = Value('i', 0)
    p = mp.Process(target=multiBTRX, args=(q, btrx, num))
    p.start()
    #print()
    input('press enter to exit.')
    #position = q.get()
    num.value = 1
    p.join()

"""
with open('position.pickle', 'wb') as handle:
    pickle.dump(position, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open('position.pickle', 'rb') as handle:
    loaded_position = pickle.load(handle)

print(loaded_position)
"""

#print(btrx.getOrder('9b4608c1-414e-486b-b284-34b97f7857b2'))

#cprUser = CryptopiaUser(API_KEY, API_SECRET)
#print(cprUser.getMarket())
#print(cprUser.get_balance())

#hitbtc = hitBTC()
#print(hitbtc.getBalance())

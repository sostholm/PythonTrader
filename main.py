

#crpUser = CryptopiaUser(API_KEY, API_SECRET)

#crpUser.getMarket()
#crpUser.get_currencies()

#from coinigy_socket import coinigy_socket
from exchange_wrappers.artificial_exchange import ArtificialExchangeWrapper
from trader.trader_hub import TraderHub
import multiprocessing as mp
from multiprocessing import Value

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
#btrx = BittrexWrapper()
#
ae = ArtificialExchangeWrapper()

#btrx = BittrexWrapper(API_KEY_BTRX, API_SECRET_BTRX)
#print(btrx.getBalance())
#print(btrx.get_markets())
#print(btrx.get_ticker('BTC-XRP'))
#print(btrx.get_ticker('BTC-LTC'))
#print(btrx.getBalance('XRP'))
#print(btrx.getOrderHistory('BTC-XRP'))

def multiBTRX(q, exchange, num):
    tr_hub = TraderHub(exchange, q, num)

if __name__ == '__main__':
    mp.set_start_method('spawn')
    q = mp.Queue()
    num = Value('i', 0)
    p = mp.Process(target=multiBTRX, args=(q, ae, num))
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



#cprUser = CryptopiaUser(API_KEY, API_SECRET)
#print(cprUser.getMarket())
#print(cprUser.get_balance())

#hitbtc = hitBTC()
#print(hitbtc.getBalance())

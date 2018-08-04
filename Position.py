class Position(object):

    def __init__(self, currency='', amount=0, exchange='', uuid='', price=0, order_type='buy', timestamp='', pair='', weight=10):
        self.entry_price = price
        self.order_type = order_type
        self.amount = amount
        self.current_price = price
        self.currency = currency
        self.exchange = exchange
        self.uuid = uuid
        self.external_uuid = ''
        self.last_high = price
        self.last_low = price
        self.hold = True
        self.timestamp = timestamp
        self.pair = pair
        self.weight = weight


    def __str__(self):
        return self.getAsDict()
    def __repr__(self):
        return self.getAsDict()
    def __eq__(self, other):
        return self.currency == other.currency

    def getAsDict(self):
        return {'entry_price' : self.entry_price,
                     'order_type':self.order_type,
                     'amount':self.amount,
                     'current_price': self.current_price,
                     'currency':self.currency,
                     'exchange':self.exchange,
                     'uuid':self.uuid,
                     'last_high':self.last_high,
                     'last_low':self.last_low,
                     'hold':self.hold,
                     'timestamp':self.timestamp,
                     'pair':self.pair
                     'weight': self.weight}

    def loadFromDict(self, dictionary):
        self.entry_price = dictionary['entry_price']
        self.order_type = dictionary['order_type']
        self.amount = dictionary['amount']
        self.current_price = dictionary['current_price']
        self.currency = dictionary['currency']
        self.exchange = dictionary['exchange']
        self.uuid = dictionary['uuid']
        self.last_high = dictionary['last_high']
        self.last_low = dictionary['last_low']
        self.hold = dictionary['hold']
        self.timestamp = dictionary['timestamp']
        self.pair = dictionary['pair']
        self.weight = dictionary['weight']


    def flip_order_type(self):
        if self.order_type == 'buy':
            self.order_type = 'sell'
        else:
            self.order_type ='buy'
        self.hold = True

    def update(self, current_price):
        self.current_price = current_price
        high =  current_price / self.last_high
        low = current_price / self.last_low

        if high > 1.0:
            self.last_high = current_price
            return 'High updated'

        elif low < 1.0:
            self.last_low = current_price
            return 'Low updated'

        return 'No updates'
    """
            if high < 1.0 and self.order_type == 'buy':
                if self.trade(current_price):
                    return 'Profit not high enough'
                else:
                    return 'Profit high enough, sell'

            elif low > 1.0 and self.order_type == 'sell':
                if self.trade(current_price):
                    return 'Profit not high enough'
                else:
                    return 'Profit high enough, buy'
    """
    """
        def trade(self, current_price):
            self.hold = True
            profit = current_price / self.entry_price
            high =  current_price / self.last_high
            low = current_price / self.last_low
            #print('profit: ' +str(profit) +' high: '+str(high)+' low: '+ str(low) )
            if self.order_type == 'buy':
                if high < 0.93  and profit > 1.01:
                    self.hold = False
                    print('trade confirmed')

            else:
                if low > 1.05 and profit < 0.95:
                    self.hold = False

            return self.hold
    """

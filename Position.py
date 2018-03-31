class Position(object):

    def __init__(self, currency='', amount=0, exchange='', uuid='', price=0, order_type='buy', timestamp='', pair=''):
        self.entry_price = price
        self.order_type = order_type
        self.amount = amount
        self.current_price = price
        self.currency = currency
        self.exchange = exchange
        self.uuid = uuid
        self.last_high = price
        self.last_low = price
        self.hold = True
        self.timestamp = timestamp
        self.pair = pair

    def __str__(self):
        return self.currency + " " + str(self.amount)
    def __repr__(self):
        return self.currency + " " + str(self.amount)


    def trade(self, current_price):
        self.hold = True
        profit = current_price / self.entry_price
        high =  current_price / self.last_high
        low = current_price / self.last_low

        if self.order_type == 'buy':
            if high < 0.93  and profit > 1.05:
                self.hold = False

        else:
            if low > 1.05 and profit < 0.95:
                self.hold = False

        return self.hold

    def update(self, current_price):
        self.current_price = current_price
        high =  current_price / self.last_high
        low = current_price / self.last_low
        return_val = 'No updates'

        if high > 1.0 and self.order_type == 'buy':
            self.last_high = current_price
            return_val = 'High updated'

        elif low < 1.0 and self.order_type == 'sell':
            self.last_low = current_price
            return_val = 'Low updated'

        if high < 1.0 and self.order_type == 'buy':
            return self.trade(current_price)

        elif low > 1.0 and self.order_type == 'sell':
            return self.trade(current_price)
        else:
            return return_val

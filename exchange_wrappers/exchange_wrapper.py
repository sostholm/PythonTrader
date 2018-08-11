from abc import abstractmethod, ABCMeta


class ExchangeWrapper(object, metaclass=ABCMeta):

    """
    ExchangeWrapper is an abstract super class.

    It contains methods that allow subclasses to communicate with crypto exchange_wrappers REST APIs
    """

    def __init__(self):
        pass

    @abstractmethod
    def _public_call(self, request_param):
        pass
    @abstractmethod
    def _private_call(self, request_param):
        pass

    @abstractmethod
    def _api_sign(self, request_url):
        pass

    @abstractmethod
    def _wait(self):
        pass

    @abstractmethod
    def get_markets(self):
        pass

    @abstractmethod
    def get_ticker(self, market):
        pass

    @abstractmethod
    def get_balances(self):
        pass

    @abstractmethod
    def get_balance(self, currency):
        pass

    @abstractmethod
    def get_order_history(self, currency):
        pass

    @abstractmethod
    def get_order(self, uuid):
        pass

    @abstractmethod
    def buy_limit(self, market, quantity, rate):
        pass

    @abstractmethod
    def sell_limit(self, market, quantity, rate):
        pass

    @abstractmethod
    def cancel_order(self, uuid):
        pass

    @abstractmethod
    def get_open_orders(self, market):
        pass

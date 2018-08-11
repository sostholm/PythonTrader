from abc import abstractmethod, ABCMeta



class MarketDataWrapper(object, metaclass=ABCMeta):

    def __init__(self):
        pass

    @abstractmethod
    def _make_api_call(self, params):
        pass

    @abstractmethod
    def _wait(self):
        pass

    @abstractmethod
    def get_all_historical_data_for_currency(self, pairs):
        pass

    @abstractmethod
    def get_all_historical_data_for_currency_between_dates(self, pairs):
        pass

    @abstractmethod
    def get_hourly_data_for_currency(self, pairs):
        pass

    @abstractmethod
    def get_hourly_data_for_currencies(self, pairs):
        pass

    @abstractmethod
    def get_minute_data_for_currency(self, pairs):
        pass

    @abstractmethod
    def get_minute_data_for_currencies(self, pairs):
        pass

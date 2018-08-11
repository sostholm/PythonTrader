import pytest
from market_data.crypto_compare_wrapper import CryptoCompareWrapper


def test_get_all_data_for_btc():
    crypto_compare = CryptoCompareWrapper()
    assert "Success" == crypto_compare.get_all_historical_data_for_currency(('BTC', 'USD'))["Response"]


def test_get_all_data_for_btc_and_ltc():
    crypto_compare = CryptoCompareWrapper()
    assert "Success" == crypto_compare.get_all_historical_data_for_currencies(('BTC,LTC', 'USD'))["Response"]

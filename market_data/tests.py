# noinspection PyUnresolvedReferences
import pytest
from market_data.crypto_compare_wrapper import CryptoCompareWrapper


def test_get_all_data_for_btc():
    crypto_compare = CryptoCompareWrapper()
    assert "Success" == crypto_compare.get_all_historical_data_for_currency(('BTC', 'USD'))["Response"]


def test_get_btc_data_from_today_and_30_days_back():
    crypto_compare = CryptoCompareWrapper()
    assert "Success" == crypto_compare.get_all_historical_data_for_currency_from_today(('BTC', 'USD'), 30)["Response"]


def test_get_btc_hours_data_30():
    crypto_compare = CryptoCompareWrapper()
    assert "Success" == crypto_compare.get_hourly_data_for_currency(('BTC', 'USD'), 24)["Response"]


def test_get_btc_minutes_data_30():
    crypto_compare = CryptoCompareWrapper()
    assert "Success" == crypto_compare.get_minute_data_for_currency(('BTC', 'USD'), 30)["Response"]

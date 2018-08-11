import pytest
from exchange_wrappers.config import KEYS
from exchange_wrappers.bittrex_wrapper import BittrexWrapper


def test_default():
    assert True


def test_public_call_bittrex():
    exchange = BittrexWrapper(KEYS['API_KEY_BTRX'], KEYS['API_SECRET_BTRX'])
    response = exchange.get_markets()
    assert response['success']


def test_private_call_get_balances():
    exchange = BittrexWrapper(KEYS['API_KEY_BTRX'], KEYS['API_SECRET_BTRX'])
    response = exchange.get_balances()
    assert response['success']

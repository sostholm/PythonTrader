import pytest
from market_data.data_manager import DataManager
from datetime import datetime as dt

def test_instance():
    manager = DataManager(10)
    assert True


def test_dataframe_data():
    manager = DataManager(10)
    df = manager.market_data
    print(df.head())
    assert len(df) > 0


def test_update():
    manager = DataManager(10)
    manager.update()


def test_update_latest_date():
    manager = DataManager(10)
    market_data = manager.update()
    date = market_data.index.max()
    print(date)

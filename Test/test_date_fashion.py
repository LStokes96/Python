import pytest
from Code import date_fashion

def test_date():
    assert date_fashion.date_fashion(6,7) == 1

def test_date():
    assert date_fashion.date_fashion(2,10) == 0

def test_date():
    assert date_fashion.date_fashion(10,5) == 2
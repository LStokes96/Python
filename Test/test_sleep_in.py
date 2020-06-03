import pytest
from Code import Sleep_in

def test_sleep_in():
    assert Sleep_in.sleep_in(True,False) == False


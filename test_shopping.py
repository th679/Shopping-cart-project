import datetime
import pytest

from shopping_cart import to_usd, human_friendly_timestamp

def test_to_usd():
    assert to_usd(5) == "$5.00"
    assert to_usd(5.777) == "$5.78"
    assert to_usd(12345) == "$12,345.00"

def test_human_friendly_timestamp():
    date = datetime.datetime(2019, 1, 1, 12, 30, 0)
    assert human_friendly_timestamp(date) == "2019-1-1 12:30:00"
    date2 = datetime.datetime(2019, 1, 1, 14, 30, 0)
    assert human_friendly_timestamp(date2) == "2019-1-1 2:30:00"


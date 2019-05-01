import datetime
import pytest

from shopping_cart import to_usd, human_friendly_timestamp, find_product, calculate_subtotal, calculate_total

def test_to_usd():
    assert to_usd(5) == "$5.00"
    assert to_usd(5.777) == "$5.78"
    assert to_usd(12345) == "$12,345.00"

def test_human_friendly_timestamp():
    date = datetime.datetime(2019, 1, 1, 12, 30, 0)
    assert human_friendly_timestamp(date) == "2019-01-01 12:30:00 PM"
    date2 = datetime.datetime(2019, 1, 1, 14, 30, 0)
    assert human_friendly_timestamp(date2) == "2019-01-01 02:30:00 PM"

def test_find_product():
    products = [
        {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":4, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":3, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99}
    ]
    matching_product = find_product(4, products) 
    assert matching_product["name"] == "Robust Golden Unsweetened Oolong Tea"
    assert matching_product["price"] == 2.49
    matching_product_str = find_product("4", products)
    assert matching_product_str["name"] == "Robust Golden Unsweetened Oolong Tea"

    with pytest.raises(IndexError):
        find_product(20, products)

def test_calculate_subtotal():
    products = [
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":4, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":3, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99}
    ]
    running_total = 0
    for product in products:
        running_total = calculate_subtotal(running_total, product["price"])
    assert running_total == 14.47

def test_calculate_total():
    subtotal = 100
    tax = 10
    assert calculate_total(subtotal, tax) == 110


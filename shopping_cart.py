# shopping-cart.py

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

# TODO: write some Python code here to produce the desired functionality...

import datetime

def to_usd(price):
    return "${0:,.2f}".format(price)

def human_friendly_timestamp(time):
    return time.strftime("%Y-%m-%d %I:%M:%S %p")

def find_product(id, products):
    matching_products = [p for p in products if str(p["id"]) == str(id)]
    matching_product = matching_products[0]
    return matching_product

def calculate_subtotal(running_total, product_price):
    subtotal = running_total + product_price
    return subtotal


def calculate_total(subtotal, tax):
    total_cost = subtotal + tax
    return total_cost


if __name__ == "__main__":

    t = datetime.datetime.now()

    selected_ids = []

    while True:
        selected_id = input("Please input a product id or DONE when finished: ")
        if selected_id == "DONE":
            break
        else:
            selected_ids.append(selected_id)

    running_total = 0

    print("----------------------------------------")
    print("FRESH FOOD MARKET")
    print("----------------------------------------")
    print("Web: www.freshfoodmarket.com")
    print("Phone: 1.202.687.0100")
    print("Checkout Time: " + human_friendly_timestamp(t))
    print("----------------------------------------")

    print("SHOPPING CART ITEMS: ")

    for selected_id in selected_ids:
        matching_product = find_product(selected_id, products)
        running_total = calculate_subtotal(running_total, matching_product["price"])
        print("+ " + matching_product["name"] + " " + to_usd(matching_product["price"]))

    sales_tax = running_total*.06
    total_cost = calculate_total(running_total, sales_tax)

    print("----------------------------------------")
    print("Subtotal: " + to_usd(running_total))
    print("Plus District of Columbia Sales Tax (6%): " + to_usd(sales_tax))
    print("Total: " + to_usd(total_cost))
    print("----------------------------------------")
    print("Thanks for shopping at Fresh Food Market! Please come again.")

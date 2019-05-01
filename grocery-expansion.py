import csv

products = []

csv_file_path = "products.csv"

with open(csv_file_path, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        d = {"id": row["id"], "name": row["name"], "price": float(row["price"])}
        products.append(d)

import datetime

t = datetime.datetime.now()

selected_ids = []

running_total = 0
while True:
    selected_id = input("Please input a product id or DONE when finished: ")
    if selected_id == "DONE":
         break
    else:
        selected_ids.append(selected_id)

print("----------------------------------------")
print("FRESH FOOD MARKET")
print("----------------------------------------")
print("Web: www.freshfoodmarket.com")
print("Phone: 1.202.687.0100")
print("Checkout Time: " + t.strftime("%Y-%m-%d %I:%M:%S %p"))
print("----------------------------------------")

print("SHOPPING CART ITEMS: ")

for selected_id in selected_ids:
    matching_products = [p for p in products if str(p["id"]) == str(selected_id)]
    matching_product = matching_products[0]
    running_total = running_total + matching_product["price"]
    price_usd = "(${0:.2f})".format(matching_product["price"])
    print("+ " + matching_product["name"] + " " + price_usd)

running_total_usd = "${0:.2f}".format(running_total)
sales_tax = running_total*.06
sales_tax_usd = "${0:.2f}".format(sales_tax)
total_cost = running_total + sales_tax
total_cost_usd =  "${0:.2f}".format(total_cost)

print("----------------------------------------")
print("Subtotal: " + running_total_usd)
print("Plus District of Columbia Sales Tax (6%): " + sales_tax_usd)
print("Total: " + total_cost_usd)
print("----------------------------------------")
print("Thanks for shopping at Fresh Food Market! Please come again.")
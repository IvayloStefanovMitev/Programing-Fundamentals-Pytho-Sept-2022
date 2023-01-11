products = input().split()
stock = {}
for product in range(0, len(products), 2):
    key = products[product]
    value = products[product + 1]
    stock[key] = value
items = input().split()
for item in items:
    if item in stock.keys():
        print(f"We have {stock[item]} of {item} left")
    else:
        print(f"Sorry, we don't have {item}")
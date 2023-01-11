products = input().split()
bakery = {}

for product in range(0, len(products), 2):
    key = products[product]
    value = products[product + 1]
    bakery[key] = int(value)
print(bakery)

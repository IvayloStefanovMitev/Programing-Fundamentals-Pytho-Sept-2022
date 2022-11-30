product_price = {}
products_quantity = {}

while True:
    command = input()
    if command == 'buy':
        break
    product, price, quantity = command.split()

    if product not in products_quantity.keys():

        products_quantity[product] = 0
        product_price[product] = 0
    products_quantity[product] += int(quantity)
    product_price[product] = float(price)

for product, quantity in products_quantity.items():
    price = quantity * product_price[product]
    print(f"{product} -> {price:.2f}")
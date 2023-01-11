products = {}
while True:

    command = input()

    if command == 'statistics':
        break

    key, value = command.split(': ')
    if key not in products.keys():
        products[key] = 0
    products[key] += int(value)
print("Products in stock:")
for key, value in products.items():
    print(f'- {key}: {value}')
print(f'Total Products: {len(products)}')
print(f'Total Quantity: {sum(int(quantity) for quantity in products.values())}')


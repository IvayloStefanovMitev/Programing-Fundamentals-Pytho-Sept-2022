def orders(type_product, num):
    if type_product == 'coffee':
        return f'{num * 1.5:.2f}'
    elif type_product == 'water':
        return f'{num * 1:.2f}'
    elif type_product == 'coke':
        return f'{num * 1.4:.2f}'
    elif type_product == 'snacks':
        return f'{num * 2:.2f}'


product = input()
quantity = int(input())
print(orders(product, quantity))
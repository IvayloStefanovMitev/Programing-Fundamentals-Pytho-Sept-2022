def rearrange_func(product, products):
    if product in products:
        products_list.append(product)
        products_list.remove(product)
    return products


def correct_func(product1, product2, products):
    if product1 in products:
        for index in range(len(products)):
            if products[index] == product1:
                products[index] = product2
    return products


def unnecessary_func(product, products):
    if product in products:
        products_list.remove(product)
    return products


def urgent_func(product, products):
    if product not in products:
        products_list.insert(0, product)
    return products


def shopping_list(products):

    while True:
        command = input()

        if command == 'Go Shopping!':
            break

        if 'Urgent' in command:
            priority, product = command.split()
            products = urgent_func(product, products)
        elif 'Unnecessary' in command:
            priority, product = command.split()
            products = unnecessary_func(product, products)
        elif 'Correct' in command:
            priority, product1, product2 = command.split()
            products = correct_func(product1, product2, products)
        elif 'Rearrange' in command:
            priority, product = command.split()
            products = rearrange_func(product, products)
    result = ', '.join(product for product in products)
    return result


products_list = input().split('!')
print(shopping_list(products_list))
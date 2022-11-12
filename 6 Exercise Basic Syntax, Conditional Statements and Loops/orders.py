number_of_orders = int(input())
total_price = 0
for order in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsule_per_day = int(input())

    if price_per_capsule < 0.01 or price_per_capsule > 100:
        continue
    elif days < 1 or days > 31:
        continue
    elif capsule_per_day < 1 or capsule_per_day > 2000:
        continue
    else:
        coffee_price = price_per_capsule * days * capsule_per_day
        total_price += coffee_price

    print(f'The price for the coffee is: ${coffee_price:.2f}')

print(f"Total: ${total_price:.2f}")
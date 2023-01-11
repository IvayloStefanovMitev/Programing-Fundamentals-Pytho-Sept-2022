import re
final_price = 0
bought_furniture = []
pattern = r'>>([a-zA-Z]+)<<([0-9]+\.?[0-9]+)!([0-9]+)'
while True:
    purchases = input()
    if purchases == 'Purchase':
        break
    result = re.findall(pattern, purchases)
    for match in result:
        furniture, price, quantity = match
        final_price += float(price) * int(quantity)
        bought_furniture.append(furniture)

print('Bought furniture:')
for curr_furniture in bought_furniture:
    print(curr_furniture)
print(f'Total money spend: {final_price:.2f}')
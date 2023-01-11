cnt_price = 0

while True:
    prices = input()
    if prices == 'special' or prices == 'regular':
        break

    curr_price = float(prices)
    if curr_price < 0:
        print("Invalid price!")
        continue
    cnt_price += curr_price
if prices == 'special':
    price_with_taxes = cnt_price * 0.2
    final_price = price_with_taxes + cnt_price
    discount = final_price - (final_price * 0.1)
    if discount == 0:
        print("Invalid order!")
    else:
        print(f"Congratulations you've just bought a new computer!\nPrice without taxes: {cnt_price:.2f}$\n"
              f"Taxes: {price_with_taxes:.2f}$\n-----------\nTotal price: {discount:.2f}$")
elif prices == 'regular':
    price_with_taxes = cnt_price * 0.2
    final_price = price_with_taxes + cnt_price
    if final_price == 0:
        print("Invalid order!")
    else:
        print(f"Congratulations you've just bought a new computer!\nPrice without taxes: {cnt_price:.2f}$\n"
              f"Taxes: {price_with_taxes:.2f}$\n-----------\nTotal price: {final_price:.2f}$")

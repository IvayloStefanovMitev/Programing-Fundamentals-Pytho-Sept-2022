import re

number = int(input())

pattern = r'(\@\#+)([A-Z][A-Za-z0-9]{4,}[A-Z])(\@\#+)'

for match in range(number):
    characters = input()
    result = re.match(pattern, characters)

    if not result:
        print("Invalid barcode")
    else:
        digits = re.findall("\d", result.group())

        if not digits:
           print("Product group: 00")

        else:
            print(f"Product group: {''.join(digits)}")


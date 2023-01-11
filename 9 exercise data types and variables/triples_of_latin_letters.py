number = int(input())
for first_char in range(number):
    for second_char in range(number):
        for third_char in range(number):
            print(f'{chr(first_char + 97) }{chr(second_char + 97)}{chr(third_char + 97)}')
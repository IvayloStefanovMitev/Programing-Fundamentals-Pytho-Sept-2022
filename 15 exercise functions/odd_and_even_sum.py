def odd_and_even_num(num):
    even_number = 0
    odd_number = 0

    for curr_number in num:
        if int(curr_number) % 2 == 0:
            even_number += int(curr_number)
        if int(curr_number) % 2 != 0:
            odd_number += int(curr_number)
    return f"Odd sum = {odd_number}, Even sum = {even_number}"


number = input()
result = odd_and_even_num(number)
print(result)
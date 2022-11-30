numbers = input().split()
lst_of_numbers = []
for number in numbers:
    lst_of_numbers.append(int(number))
result = filter(lambda curr_number: curr_number % 2 == 0, lst_of_numbers)
print(list(result))
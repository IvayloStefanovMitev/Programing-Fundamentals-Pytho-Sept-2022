numbers = input().split()
lst_of_numbers = []
for number in numbers:
    lst_of_numbers.append(int(number))
result = sorted(lst_of_numbers)
print(list(result))
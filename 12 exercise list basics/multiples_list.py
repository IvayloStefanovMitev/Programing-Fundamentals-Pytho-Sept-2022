factor = int(input())
count = int(input())
list_of_numbers = []
for number in range(1, count + 1):
    curr_number = number * factor
    list_of_numbers.append(curr_number)


print(list_of_numbers)
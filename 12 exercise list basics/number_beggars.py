numbers = input().split(', ')
beggars = int(input())
final_numbers = []
numbers_as_digit = []
starting_index = 0
for number in numbers:
    curr_number = int(number)
    numbers_as_digit.append(curr_number)
while starting_index < beggars:
    curr_number_beggar = 0
    for curr_index in range(starting_index, len(numbers_as_digit), beggars):
        curr_number_beggar += numbers_as_digit[curr_index]
    final_numbers.append(curr_number_beggar)
    starting_index += 1
print(final_numbers)
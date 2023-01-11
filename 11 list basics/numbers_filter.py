single_number = int(input())
COMMAND_EVEN = 'even'
COMMAND_ODD = 'odd'
COMMAND_NEGATIVE = 'negative'
COMMAND_POSITIVE = 'positive'
lst_of_number = []
lst_of_filtered_numbers = []

for curr_number in range(single_number):
    numbers = int(input())
    lst_of_number.append(numbers)
command = input()
for number in lst_of_number:

    filtered_number_passes = (
        (command == COMMAND_EVEN and number % 2 == 0) or
        (command == COMMAND_ODD and number % 2 != 0) or
        (command == COMMAND_NEGATIVE and number < 0) or
        (command == COMMAND_POSITIVE and number >= 0)
    )

    if filtered_number_passes:
        lst_of_filtered_numbers.append(number)
print(lst_of_filtered_numbers)
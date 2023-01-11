
def multiply_func(first_num, second_num, values):
    multiply_result = values[first_num] * values[second_num]
    array_values.insert(first_num, multiply_result)
    array_values.pop(first_num + 1)
    return values


def swap_func(first_num, second_num, values):
    values[first_num], values[second_num] = values[second_num], values[first_num]
    return values


def array_modifier_func(values):
    while True:
        command = input()
        if command == 'end':
            break
        if command == 'decrease':
            for value in range(len(values)):
                values[value] -= 1

        if 'swap' in command:
            curr_command, index1, index2 = command.split()
            values = swap_func(int(index1), int(index2), values)
        elif 'multiply' in command:
            curr_command, index1, index2 = command.split()
            values = multiply_func(int(index1), int(index2), values)

    final_result = ', '.join(str(num) for num in values)
    print(final_result)


array_values = list(map(int, input().split()))
array_modifier_func(array_values)
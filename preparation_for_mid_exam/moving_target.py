def strike_func(first_num, second_num, targets):
    if 0 <= first_num < len(targets) and 0 <= first_num - int(second_num) < len(targets) and 0 <= first_num\
            + int(second_num) < len(targets):
        first_index = first_num - second_num
        last_index = first_num + second_num
        targets = [targets[curr_target] for curr_target in range(len(targets))\
                   if curr_target < first_index or curr_target > last_index]
    else:
        print("Strike missed!")
    return targets


def add_func(first_num, second_num, targets):
    if 0 <= first_num < len(targets):
        targets_values.insert(first_num, second_num)
    else:
        print("Invalid placement!")
    return targets


def shoot_func(first_num, second_num, targets):
    if 0 <= first_num < len(targets):
        targets[first_num] -= second_num
        if targets[first_num] <= 0:
            targets_values.remove(targets[first_num])
    return targets


def moving_target(targets):

    while True:
        command = input()
        if command == 'End':
            break
        curr_command, value1, value2 = command.split()
        if curr_command == 'Shoot':
            targets = shoot_func(int(value1), int(value2), targets)
        elif curr_command == 'Add':
            targets = add_func(int(value1), int(value2), targets)
        elif curr_command == 'Strike':
            targets = strike_func(int(value1), int(value2), targets)

    result = '|'.join(str(num) for num in targets)
    return result


targets_values = list(map(int, input().split()))
print(moving_target(targets_values))
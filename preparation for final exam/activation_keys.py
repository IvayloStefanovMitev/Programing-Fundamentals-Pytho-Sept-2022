def slice_func(start_index, end_index, raw_key):
    raw_key = raw_key[:start_index] + raw_key[end_index:]
    print(raw_key)

    return raw_key


def flip_func(upper_lower, start_index, end_index, raw_key):
    if 'Upper' in upper_lower:
        raw_key = raw_key[:start_index] + raw_key[start_index:end_index].upper() + raw_key[end_index:]
        print(raw_key)
    elif 'Lower' in upper_lower:
        raw_key = raw_key[:start_index] + raw_key[start_index:end_index].lower() + raw_key[end_index:]
        print(raw_key)

    return raw_key


def substring_func(substring, raw_key):
    if substring in raw_key:
        print(f"{raw_key} contains {substring}")
    else:
        print("Substring not found!")

    return raw_key


def activation_keys(raw_key):

    while True:
        command = input().split('>>>')
        curr_command = command[0]
        if curr_command == 'Generate':
            break

        if curr_command == 'Contains':
            substring = command[1]
            raw_key = substring_func(substring, raw_key)
        elif curr_command == 'Flip':
            upper_lower = command[1]
            start_index = int(command[2])
            end_index = int(command[3])
            raw_key = flip_func(upper_lower, start_index, end_index, raw_key)
        elif curr_command == 'Slice':
            start_index = int(command[1])
            end_index = int(command[2])
            raw_key = slice_func(start_index, end_index, raw_key)

    print(f"Your activation key is: {raw_key}")


raw_activation_key = input()
activation_keys(raw_activation_key)
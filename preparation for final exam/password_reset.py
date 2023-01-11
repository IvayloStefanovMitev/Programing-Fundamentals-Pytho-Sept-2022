def substitute_func(substring, substitute, string):
    if substring in string:
        string = string.replace(substring, substitute)
        print(string)
    else:
        print("Nothing to replace!")
    return string


def cut_func(index, length, string):
    string = string[:index] + string[index + length:]
    print(string)
    return string


def odd_func(string):
    new_string = ''
    for letter in range(len(string)):
        if letter % 2 != 0:
            new_string += string[letter]
    print(new_string)
    return new_string


def reset_password(string):

    while True:
        command = input().split()
        curr_command = command[0]
        if curr_command == 'Done':
            break

        if curr_command == 'TakeOdd':
            string = odd_func(string)
        elif curr_command == 'Cut':
            index = int(command[1])
            length = int(command[2])
            string = cut_func(index, length, string)
        elif curr_command == 'Substitute':
            substring = command[1]
            substitute = command[2]
            string = substitute_func(substring, substitute, string)

    return f"Your password is: {string}"


password_string = input()
print(reset_password(password_string))
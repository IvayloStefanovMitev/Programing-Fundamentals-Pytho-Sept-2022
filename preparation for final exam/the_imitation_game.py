def change_all_func(substring, replacement, message):
    message = message.replace(substring, replacement)

    return message


def insert_func(index, value, message):
    message = message[:index] + value + message[index:]

    return message


def move_func(number_of_letter, message):
    message = message[number_of_letter:] + message[:number_of_letter]

    return message


def imitation_game(message):

    while True:
        command = input().split('|')
        curr_command = command[0]
        if curr_command == 'Decode':
            break
        if curr_command == 'Move':
            number_of_letter = int(command[1])
            message = move_func(number_of_letter, message)
        elif curr_command == 'Insert':
            index = int(command[1])
            value = command[2]
            message = insert_func(index, value, message)
        elif curr_command == 'ChangeAll':
            substring = command[1]
            replacement = command[2]
            message = change_all_func(substring, replacement, message)

    return f"The decrypted message is: {message}"


encrypted_message = input()
print(imitation_game(encrypted_message))
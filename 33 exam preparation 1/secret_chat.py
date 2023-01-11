def change_func(substring, replacement, message):
    message = message.replace(substring, replacement)
    print(message)
    return message


def substring_func(substring, message):
    if substring in message:
        message = message.replace(substring, '', 1)
        message = message + substring[::-1]
    else:
        print('error')
        return message
    print(message)
    return message


def insert_func(index, message):
    result = message[:index] + ' ' + message[index:]
    print(result)
    return result


def secret_chat(message):
    while True:
        command = input().split(':|:')
        curr_command = command[0]

        if curr_command == 'Reveal':
            break
        if curr_command == 'InsertSpace':
            index = int(command[1])
            message = insert_func(index, message)
        elif curr_command == 'Reverse':
            substring = command[1]
            message = substring_func(substring, message)
        elif curr_command == 'ChangeAll':
            substring = command[1]
            replacement = command[2]
            message = change_func(substring, replacement, message)

    return f"You have a new text message: {message}"


concealed_message = input()
print(secret_chat(concealed_message))
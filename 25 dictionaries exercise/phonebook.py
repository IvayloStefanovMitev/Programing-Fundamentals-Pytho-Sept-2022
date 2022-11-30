phonebook = {}

while True:
    command = input()
    if '-' not in command:
        break
    curr_command = command.split('-')
    for names in range(0, len(curr_command), 2):
        name = curr_command[names]
        number = curr_command[names + 1]
        phonebook[name] = number
for num in range(int(command)):
    curr_name = input()
    if curr_name in phonebook.keys():
        print(f"{curr_name} -> {phonebook[curr_name]}")
    else:
        print(f"Contact {curr_name} does not exist.")
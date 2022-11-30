wagons = int(input())
train = [0] * wagons
while True:
    command = input()
    if command == 'End':
        break
    lst_command = command.split()
    curr_command = lst_command[0]

    if curr_command == 'add':
        train[-1] += int(lst_command[1])
    elif curr_command == 'insert':
        curr_wagon = int(lst_command[1])
        train[curr_wagon] += int(lst_command[2])
    elif curr_command == 'leave':
        curr_wagon = int(lst_command[1])
        train[curr_wagon] -= int(lst_command[2])

print(train)
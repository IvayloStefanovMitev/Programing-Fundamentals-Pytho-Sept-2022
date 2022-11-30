task = {}
while True:

    command = input()

    if command == 'stop':
        break

    quantity = int(input())
    if command not in task.keys():
        task[command] = 0

    task[command] += quantity
for resource, quantity in task.items():
    print(f"{resource} -> {quantity}")


company_users = {}
while True:
    command = input()
    if command == 'End':
        break
    name, id_number = command.split(' -> ')
    if name not in company_users.keys():
        company_users[name] = []
    if id_number not in company_users[name]:
        company_users[name].append(id_number)

for name, id_number in company_users.items():
    print(f'{name}')
    for curr_id in id_number:
        print(f'-- {curr_id}')
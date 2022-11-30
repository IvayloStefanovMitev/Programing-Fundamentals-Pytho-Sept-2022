softuni_parking = {}
cars = int(input())
for car in range(cars):
    command = input().split()
    action = command[0]

    if action == 'register':
        name = command[1]
        plate_number = command[2]
        if name not in softuni_parking.keys():

            softuni_parking[name] = plate_number

            print(f'{name} registered {softuni_parking[name]} successfully')
        elif name in softuni_parking.keys():
            print(f'ERROR: already registered with plate number {softuni_parking[name]}')

    elif action == 'unregister':
        name = command[1]
        if name not in softuni_parking.keys():
            print(f"ERROR: user {name} not found")
        else:
            del softuni_parking[name]
            print(f"{name} unregistered successfully")

for name, plate_number in softuni_parking.items():

    print(f'{name} => {plate_number}')





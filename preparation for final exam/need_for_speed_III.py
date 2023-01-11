def revert_func(car, kilometers, all_cars):
    all_cars[car][0] = int(all_cars[car][0]) - kilometers
    if all_cars[car][0] < 10000:
        all_cars[car][0] = 10000

    else:
        print(f"{car} mileage decreased by {kilometers} kilometers")
    return all_cars


def refuel_func(car, fuel, all_cars):
    amount_refueled = int(all_cars[car][1]) + fuel
    if amount_refueled <= 75:
        all_cars[car][1] = amount_refueled
        print(f'{car} refueled with {fuel} liters')
    else:
        needed_amount = abs(int(all_cars[car][1]) - 75)
        all_cars[car][1] = 75
        print(f'{car} refueled with {needed_amount} liters')

    return all_cars


def drive_func(car, distance, fuel, all_cars):
    if all_cars[car][1] < fuel:
        print('Not enough fuel to make that ride')

    elif all_cars[car][0] <= 100000:
        all_cars[car][0] = distance + int(all_cars[car][0])
        all_cars[car][1] = int(all_cars[car][1]) - fuel
        print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
    if all_cars[car][0] >= 100000:
        print(f'Time to sell the {car}!')
        del all_cars[car]

    return all_cars


def cars(numbers):
    all_cars = {}
    for every_car in range(numbers):
        curr_car = input().split('|')
        car = curr_car[0]
        mileage = int(curr_car[1])
        fuel = int(curr_car[2])

        all_cars[car] = [mileage, fuel]
    return all_cars


def need_for_speed(numbers):
    all_cars = cars(numbers)

    while True:
        command = input().split(' : ')
        curr_command = command[0]

        if curr_command == 'Stop':
            break

        if curr_command == 'Drive':
            car = command[1]
            distance = int(command[2])
            fuel = int(command[3])
            all_cars = drive_func(car, distance, fuel, all_cars)
        elif curr_command == 'Refuel':
            car = command[1]
            fuel = int(command[2])
            all_cars = refuel_func(car, fuel, all_cars)
        elif curr_command =='Revert':
            car = command[1]
            kilometers = int(command[2])
            all_cars = revert_func(car, kilometers, all_cars)

    for car_name, data in all_cars.items():
        print(f"{car_name} -> Mileage: {data[0]} kms, Fuel in the tank: {data[1]} lt.")


number_of_cars = int(input())
need_for_speed(number_of_cars)
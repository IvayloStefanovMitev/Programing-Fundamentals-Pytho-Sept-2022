def reset_func(plant, all_plants):

    all_plants[plant][1] = []

    return all_plants


def update_func(plant, new_rarity, all_plants):

    all_plants[plant][0] = new_rarity

    return all_plants


def rate_func(plant, rating, all_plants):

    all_plants[plant][1].append(float(rating))

    return all_plants


def plants(number):
    all_plants = {}
    for every_plants in range(number):
        curr_plants = input().split('<->')
        plant = curr_plants[0]
        rarity = int(curr_plants[1])

        if plant not in all_plants:
            all_plants[plant] = [0, []]
        all_plants[plant][0] += rarity

    return all_plants


def plant_discovery(number):
    all_plants = plants(number)

    while True:
        command = input().split(': ')
        curr_command = command[0]
        if curr_command == 'Exhibition':
            break

        if curr_command == 'Rate':
            plant, rating = command[1].split(' - ')
            if plant in all_plants:
                all_plants = rate_func(plant, rating, all_plants)
            else:
                print('error')
        elif curr_command == 'Update':
            plant, new_rarity = command[1].split(' - ')
            if plant in all_plants:
                all_plants = update_func(plant, new_rarity, all_plants)
            else:
                print('error')
        elif curr_command == 'Reset':
            plant = command[1]
            if plant in all_plants:
                all_plants = reset_func(plant, all_plants)
            else:
                print('error')

    print('Plants for the exhibition:')

    for name_of_plant, data in all_plants.items():
        if not all_plants[name_of_plant][1]:
            print(f'- {name_of_plant}; Rarity: {data[0]}; Rating: 0.00')
        else:
            avr_rating = sum(data[1]) / len(data[1])
            print(f'- {name_of_plant}; Rarity: {data[0]}; Rating: {avr_rating:.2f}')


number_of_plants = int(input())
plant_discovery(number_of_plants)
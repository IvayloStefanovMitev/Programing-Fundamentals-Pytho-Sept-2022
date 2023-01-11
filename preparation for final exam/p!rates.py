def prosper(town, city_gold, cities):
    if city_gold < 0:
        print("Gold added cannot be a negative number!")
    else:
        cities[town][1] += city_gold
        print(f"{city_gold} gold added to the city treasury. {town} now has {cities[town][1]} gold.")

    return cities


def plunder_func(town, people, city_gold, cities):
    cities[town][0] -= people
    cities[town][1] -= city_gold
    print(f"{town} plundered! {city_gold} gold stolen, {people} citizens killed.")
    if cities[town][0] <= 0 or cities[town][1] <= 0:
        print(f"{town} has been wiped off the map!")
        del cities[town]

    return cities


def pirates(cities):

    while True:
        main_command = input().split('=>')
        curr_command = main_command[0]
        if curr_command == 'End':
            break
        if curr_command == 'Plunder':
            town = main_command[1]
            people = int(main_command[2])
            city_gold = int(main_command[3])
            cities = plunder_func(town, people, city_gold, cities)
        elif curr_command == 'Prosper':
            town = main_command[1]
            city_gold = int(main_command[2])
            cities = prosper(town, city_gold, cities)

    if cities:
        print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
        for city_name, data in cities.items():
            print(f"{city_name} -> Population: {data[0]} citizens, Gold: {data[1]} kg")
    else:
        print("Ahoy, Captain! All targets have been plundered and destroyed!")


city_information = input()
all_cities = {}
while city_information != 'Sail':
    curr_city = city_information.split('||')
    command = curr_city[0]

    population = int(curr_city[1])
    gold = int(curr_city[2])
    if command not in all_cities:
        all_cities[command] = [0, 0]
    all_cities[command][0] += population
    all_cities[command][1] += gold
    city_information = input()

pirates(all_cities)
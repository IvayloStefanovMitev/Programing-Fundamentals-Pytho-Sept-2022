def mu_online(dungeon_rooms):
    health = 100
    bitcoins = 0
    room_counter = 0
    for room in rooms:
        command, number = room.split()
        number = int(number)
        room_counter += 1
        if health <= 0:
            break
        if command == 'potion':
            health += number

            if health > 100:
                health_heal = 100 - (health - number)
                health = 100
                print(f"You healed for {health_heal} hp.")
                print(f"Current health: {health} hp.")
            elif health <= 100:
                print(f"You healed for {number} hp.")
                print(f"Current health: {health} hp.")
            else:
                continue

        elif command == 'chest':
            bitcoins += number
            print(f"You found {number} bitcoins.")

        else:
            health -= number
            if health > 0:
                print(f"You slayed {command}.")
            else:
                print(f"You died! Killed by {command}.")
                print(f"Best room: {room_counter}")

    if health > 0:
        print("You've made it!")
        print(f"Bitcoins: {bitcoins}")
        print(f"Health: {health}")
    return dungeon_rooms


rooms = input().split('|')
mu_online(rooms)
energy = int(input())
battle_won = 0
while True:
    command = input()
    if command == 'End of battle':
        print(f"Won battles: {battle_won}. Energy left: {energy}")
        break
    distance = int(command)
    if energy <= 0:
        print(f"Not enough energy! Game ends with {battle_won} won battles and {energy} energy")
        break
    if distance <= energy:
        battle_won += 1
        energy -= distance
        if battle_won % 3 == 0:
            energy += battle_won
    else:
        print(f"Not enough energy! Game ends with {battle_won} won battles and {energy} energy")
        break
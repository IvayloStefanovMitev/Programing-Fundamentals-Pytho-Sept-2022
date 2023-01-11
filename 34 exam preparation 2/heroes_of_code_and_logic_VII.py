def heal_func(hero_name, amount, all_heroes):
    amount_recovered = int(all_heroes[hero_name][0]) + amount

    if amount_recovered <= 100:
        all_heroes[hero_name][0] = amount_recovered
        print(f"{hero_name} healed for {amount} HP!")
    else:
        needed_amount = abs(int(all_heroes[hero_name][0]) - 100)
        all_heroes[hero_name][0] = 100
        print(f"{hero_name} healed for {needed_amount} HP!")
    return all_heroes


def recharge_func(hero_name, amount, all_heroes):
    amount_recovered = int(all_heroes[hero_name][1]) + amount

    if amount_recovered <= 200:
        all_heroes[hero_name][1] = amount_recovered
        print(f"{hero_name} recharged for {amount} MP!")
    else:
        needed_amount = abs(int(all_heroes[hero_name][1]) - 200)
        all_heroes[hero_name][1] = 200
        print(f"{hero_name} recharged for {needed_amount} MP!")
    return all_heroes


def take_damage_func(hero_name, damage, attacker, all_heroes):
    curr_hp = int(all_heroes[hero_name][0]) - damage
    all_heroes[hero_name][0] = curr_hp
    if curr_hp > 0:
        print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {curr_hp} HP left!")
    else:
        print(f"{hero_name} has been killed by {attacker}!")
        del all_heroes[hero_name]
    return all_heroes


def cast_spell_func(hero_name, mp_needed, spell_name, all_heroes):
    if int(all_heroes[hero_name][1]) >= mp_needed:
        mana_left = int(all_heroes[hero_name][1]) - mp_needed
        all_heroes[hero_name][1] = mana_left
        print(f"{hero_name} has successfully cast {spell_name} and now has {mana_left} MP!")
    else:
        print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    return all_heroes


def heroes(number):
    all_heroes = {}
    for every_hero in range(number):
        curr_hero = input().split()
        hero = curr_hero[0]
        hp = curr_hero[1]
        mp = curr_hero[2]

        all_heroes[hero] = [hp, mp]
    return all_heroes


def game(number):
    all_heroes = heroes(number)

    while True:
        command = input().split(' - ')
        curr_command = command[0]
        if curr_command == 'End':
            break

        if curr_command == 'CastSpell':
            hero_name = command[1]
            mp_needed = int(command[2])
            spell_name = command[3]
            cast_spell_func(hero_name, mp_needed, spell_name, all_heroes)
        elif curr_command == 'TakeDamage':
            hero_name = command[1]
            damage = int(command[2])
            attacker = command[3]
            take_damage_func(hero_name, damage, attacker, all_heroes)
        elif curr_command == 'Recharge':
            hero_name = command[1]
            amount = int(command[2])
            recharge_func(hero_name, amount, all_heroes)
        elif curr_command == 'Heal':
            hero_name = command[1]
            amount = int(command[2])
            heal_func(hero_name, amount, all_heroes)

    for name, status in all_heroes.items():
        print(f"{name}\n  HP: {status[0]}\n  MP: {status[1]}")


number_of_heroes = int(input())
game(number_of_heroes)
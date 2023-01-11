def heart_delivery(hearts):
    jump_position = 0
    while True:

        last_position_counter = 0
        command = input()
        if command == 'Love!':
            break

        curr_command, length = command.split()
        length = int(length)
        jump_position += length

        if len(hearts) > jump_position:
            if hearts[jump_position] <= 0:
                print(f"Place {jump_position} already had Valentine's day.")
            else:
                hearts[jump_position] -= 2
                if hearts[jump_position] <= 0:
                    print(f"Place {jump_position} has Valentine's day.")

        else:
            jump_position = 0
            if hearts[0] > 0:
                hearts[0] -= 2
                if hearts[0] <= 0:
                    print(f"Place {hearts[0]} has Valentine's day.")
            else:
                print(f"Place {hearts[0]} already had Valentine's day.")

    for heart in hearts:
        if heart > 0:
            last_position_counter += 1
    print(f"Cupid's last position was {jump_position}.")
    if not last_position_counter == 0:
        print(f"Cupid has failed {last_position_counter} places.")
    else:
        print("Mission was successful.")

    return hearts


needed_hearts = list(map(int, input().split('@')))
heart_delivery(needed_hearts)



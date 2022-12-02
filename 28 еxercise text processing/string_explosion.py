after_explosion_string = ''
strength_of_explosion = 0
string = input()

for index in range(len(string)):
    if strength_of_explosion > 0 and string[index] != '>':
        strength_of_explosion -= 1
    elif string[index] != '>' and strength_of_explosion == 0:
        after_explosion_string += string[index]

    elif string[index] == '>':
        strength_of_explosion += int(string[index + 1])
        after_explosion_string += string[index]

print(after_explosion_string)




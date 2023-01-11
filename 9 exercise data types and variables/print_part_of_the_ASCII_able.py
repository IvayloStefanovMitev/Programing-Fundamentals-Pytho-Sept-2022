first_index = int(input())
last_index = int(input())
for index in range(first_index, last_index + 1):
    curr_char = chr(index)
    print(f'{curr_char}', end=" ")

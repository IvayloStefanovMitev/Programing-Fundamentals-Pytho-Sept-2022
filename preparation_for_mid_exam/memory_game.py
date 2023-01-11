
elements = input().split()
number_of_moves = 0

while True:
    is_index = True
    numbers = input()
    middle_elements = len(elements) // 2

    if len(elements) == 0:
        print(f"You have won in {number_of_moves} turns!")
        break

    if numbers == 'end':
        print("Sorry you lose :(")
        print(f"{' '.join(elements)}")
        break
    numbers_int = numbers.split()
    indexes = list(map(int, numbers_int))
    number_of_moves += 1

    if indexes[0] == indexes[1]:
        is_index = False

    for index in indexes:
        if not 0 <= index < len(elements):
            is_index = False

    if not is_index:
        print("Invalid input! Adding additional elements to the board")
        elements.insert(middle_elements, f"-{number_of_moves}a")
        elements.insert(middle_elements, f"-{number_of_moves}a")
        continue

    if elements[indexes[0]] == elements[indexes[1]]:
        print(f"Congrats! You have found matching elements - {elements[0]}!")
        elements_to_remove = elements.pop(indexes[0])
        elements.remove(elements_to_remove)
    else:
        print("Try again!")
        continue
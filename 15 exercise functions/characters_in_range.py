def characters(first, second):
    lst_of_char = []
    for curr_char in range(ord(first) + 1, ord(second)):
        lst_of_char.append(chr(curr_char))
    return lst_of_char


first_char = input()
second_char = input()
result = characters(first_char, second_char)
print(' '.join(result))
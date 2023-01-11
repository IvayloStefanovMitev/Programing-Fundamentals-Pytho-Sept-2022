number_of_lines = int(input())
cunt_letters = 0
for letter in range(number_of_lines):
    curr_char = input()
    curr_letter = ord(curr_char)
    cunt_letters += curr_letter
print(f"The sum equals: {cunt_letters}")
curr_letter = ''
final_text = ''

letters = input()
for letter in letters:
    if letter != curr_letter:
        final_text += letter
        curr_letter = letter
print(final_text)



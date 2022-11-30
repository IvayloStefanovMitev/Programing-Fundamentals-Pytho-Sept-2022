text = input().split()
characters = {}
text_without_space = ''.join(text)
for letter in text_without_space:
    if letter not in characters:
        characters[letter] = 0
    characters[letter] += 1
for letter, quantity in characters.items():
    print(f"{letter} -> {quantity}")
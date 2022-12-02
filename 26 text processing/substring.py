word_to_remove = input()
word = input()
while word_to_remove in word:
    word = word.replace(word_to_remove, '')
print(word)

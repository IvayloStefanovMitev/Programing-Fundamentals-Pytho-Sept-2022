import re

sentences = input()
needed_word = input()
pattern = fr'\b{needed_word}\b'

result = re.findall(pattern, sentences, re.IGNORECASE)
print(len(result))
import re

mirror_words = []
pair_counter = 0
data = input()

pattern = r'(@|#)([A-Za-z]{3,})\1{2}([A-Za-z]{3,})\1'

result = re.findall(pattern, data)

for pair in result:
    if pair[1] == pair[2][::-1]:
        mirror_words.append(f'{pair[1]} <=> {pair[2]}')

    if result:
        pair_counter += 1

if result:
    print(f'{pair_counter} word pairs found!')
else:
    print("No word pairs found!")
if mirror_words:
    print(f"The mirror words are:\n{', '.join(mirror_words)}")
else:
    print("No mirror words!")

    
import re
mirror_words = []
pair_counter = 0
data = input()

pattern = r'(@|#)([A-Za-z]{3,})\1{2}([A-Za-z]{3,})\1'

result = re.findall(pattern, data)


for pair in result:
    if pair[1] == pair[2][::-1]:
        mirror_words.append(f'{pair[1]} <=> {pair[2]}')

    pair_counter += 1


if pair_counter > 0:
    print(f'{pair_counter} word pairs found!')
    if not mirror_words:
        print("No mirror words!")
    else:
        print(f"The mirror words are:\n{', '.join(mirror_words)}")
else:
    print("No word pairs found!")
    print("No mirror words!")



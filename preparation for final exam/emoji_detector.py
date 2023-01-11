import re

num_list = []
cool_threshold = 1
valid_emojis = 0
match_emoji = []
text = input()
for num in text:
    if num.isdigit():
        num_list.append(int(num))

for curr_num in num_list:
    cool_threshold *= curr_num
print(f"Cool threshold: {cool_threshold}")

pattern = r'(::|\*\*)([A-Z][a-z]{2,})\1'
result = re.finditer(pattern, text)
for emoji in result:
    valid_emojis += 1
    match_emoji.append(emoji.group())
print(f"{valid_emojis} emojis found in the text. The cool ones are:")
for every_emoji in match_emoji:
    ascii_letters_counter = 0
    words = re.findall("\w", every_emoji)
    for letter in words:
        ascii_letters_counter += ord(letter)
    if ascii_letters_counter >= cool_threshold:
        print(every_emoji)
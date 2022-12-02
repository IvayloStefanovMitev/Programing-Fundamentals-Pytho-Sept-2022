text = input()
for index in range(len(text)):
    if text[index] == ":":
        emoticon = text[index + 1]
        print(f":{emoticon}")


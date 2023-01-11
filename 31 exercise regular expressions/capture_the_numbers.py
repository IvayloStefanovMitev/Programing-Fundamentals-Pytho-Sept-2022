import re
sentences = input()

pattern = r'\d+'

while sentences:
    result = re.findall(pattern, sentences)
    if result:
        print(' '.join(result), end=' ')

    sentences = input()




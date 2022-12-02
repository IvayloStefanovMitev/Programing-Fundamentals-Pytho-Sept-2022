word1, word2 = input().split()
counter = 0
if len(word1) > len(word2):
    for index in range(len(word2)):
        counter += ord(word2[index]) * ord(word1[index])
    for index in range(len(word2), len(word1)):
        counter += ord(word1[index])

elif len(word1) < len(word2):
    for index in range(len(word1)):
        counter += ord(word2[index]) * ord(word1[index])
    for index in range(len(word1), len(word2)):
        counter += ord(word2[index])
else:
    for index in range(len(word2)):
        counter += ord(word2[index]) * ord(word1[index])

print(counter)
def caesar_cipher(sentence):
    encrypted_version = ''

    for index in range(len(sentence)):
        encrypted_version += chr(ord(sentence[index]) + 3)
    return encrypted_version


text = input()
print(caesar_cipher(text))


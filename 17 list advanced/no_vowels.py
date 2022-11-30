text = input()
vowels_lst = ['a', 'o', 'u', 'e', 'i']
no_vowels = [latter for latter in text if latter.lower() not in vowels_lst]
print(''.join(no_vowels))
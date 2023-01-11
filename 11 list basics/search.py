number = int(input())
word = input()
lst_of_str = []
for curr_num in range(number):
    some_str = input()
    lst_of_str.append(some_str)
print(lst_of_str)
for curr_str in range(len(lst_of_str) - 1, -1, -1):
    curr_word = lst_of_str[curr_str]
    if word not in curr_word:
        lst_of_str.remove(curr_word)
print(lst_of_str)
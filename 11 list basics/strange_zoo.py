first_word = input()
second_word = input()
third_word = input()
lst_of_words = [first_word, second_word, third_word]
lst_of_words[0], lst_of_words[2] = lst_of_words[2], lst_of_words[0]
print(lst_of_words)

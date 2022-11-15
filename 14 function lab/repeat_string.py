def repeat_string(curr_word, curr_number):
    result = curr_word * curr_number
    return result


word = input()
counter = int(input())
print(repeat_string(word, counter))
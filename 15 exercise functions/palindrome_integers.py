def palindrome(num):
    is_palindrome = False
    for curr_num in num:
        if curr_num == curr_num[::-1]:
            is_palindrome = True
            print(True)
        else:
            print(False)
    return is_palindrome


numbers = input().split(', ')
palindrome(numbers)

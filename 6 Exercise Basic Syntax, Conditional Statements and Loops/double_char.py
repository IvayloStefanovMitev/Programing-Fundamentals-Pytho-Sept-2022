some_string = input()
while some_string != 'End':
    if some_string != 'SoftUni':
        for char in some_string:
            print(char * 2, end='')
        print()
    some_string = input()
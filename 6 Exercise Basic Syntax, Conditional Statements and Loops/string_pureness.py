strings_number = int(input())
for curr_string in range(strings_number):
    type_string = input()
    if ',' in type_string or '.' in type_string or '_' in type_string:
        print(f"{type_string} is not pure!")
    else:
        print(f"{type_string} is pure.")
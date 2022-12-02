strings = input().split()
for string in strings:
    print(f'{"".join(string * len(string))}', end='')
while True:
    words = input()
    if words == 'end':
        break

    print(f'{words} = {words[::-1]}')
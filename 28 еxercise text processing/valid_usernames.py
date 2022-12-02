def redundant_symbol_func(username):
    if ' ' in username:
        return False
    return True


def contain_func(username):
    for symbol in username:
        if not(symbol.isalnum() or symbol == '-' or symbol == '_'):
            return False
    return True


def length_func(username):
    if 3 <= len(username) <= 16:
        return True
    return False


def valid_username(username):
    if length_func(username) and contain_func(username) and redundant_symbol_func(username):
        return True
    return False


names = input().split(", ")
for name in names:
    if valid_username(name):
        print(name)

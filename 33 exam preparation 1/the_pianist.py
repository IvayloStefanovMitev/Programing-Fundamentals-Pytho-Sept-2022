def pieces_number(piece):
    all_pieces = {}
    for pieces in range(piece):
        curr_pieces = input().split('|')
        key = curr_pieces[0]
        value1 = curr_pieces[1]
        value2 = curr_pieces[2]

        all_pieces[key] = [value1, value2]
    return all_pieces


def change_func(this_piece, new_key, all_pieces):
    if this_piece in all_pieces:
        all_pieces[this_piece][1] = new_key
        print(f"Changed the key of {this_piece} to {new_key}!")
    else:
        print(f"Invalid operation! {this_piece} does not exist in the collection.")


def remove_func(this_piece, all_pieces):
    if this_piece in all_pieces:
        del all_pieces[this_piece]
        print(f"Successfully removed {this_piece}!")
    else:
        print(f"Invalid operation! {this_piece} does not exist in the collection.")


def add_func(this_piece, composer, curr_key, all_pieces):
    if this_piece not in all_pieces:
        all_pieces[this_piece] = [composer, curr_key]
        print(f"{this_piece} by {composer} in {curr_key} added to the collection!")
    else:
        print(f"{this_piece} is already in the collection!")


def pianist(piece):
    all_pieces = pieces_number(piece)

    while True:
        command = input().split('|')
        curr_command = command[0]
        if curr_command == 'Stop':
            break

        if curr_command == 'Add':
            this_piece = command[1]
            composer = command[2]
            curr_key = command[3]
            add_func(this_piece, composer, curr_key, all_pieces)
        elif curr_command == 'Remove':
            this_piece = command[1]
            remove_func(this_piece, all_pieces)

        elif curr_command == 'ChangeKey':
            this_piece = command[1]
            new_key = command[2]
            change_func(this_piece, new_key, all_pieces)
    for key, value in all_pieces.items():
        print(f"{key} -> Composer: {value[0]}, Key: {value[1]}")


number_of_pieces = int(input())
pianist(number_of_pieces)
def switch_func(old_string, new_string, stops):
    stops = stops.replace(old_string, new_string)
    print(stops)

    return stops


def remove_func(start_index, end_index, stops):
    if 0 <= start_index <= end_index < len(stops):
        stops = stops[:start_index] + stops[end_index + 1:]
    print(stops)

    return stops


def add_func(index, string, stops):
    if 0 <= index < len(stops):
        stops = stops[:index] + string + stops[index:]
    print(stops)

    return stops


def word_tour(stops):
    while True:
        command = input().split(':')
        curr_command = command[0]
        if curr_command == 'Travel':
            break
        elif curr_command == 'Add Stop':
            index = int(command[1])
            string = command[2]
            stops = add_func(index, string, stops)
        elif curr_command == 'Remove Stop':
            start_index = int(command[1])
            end_index = int(command[2])
            stops = remove_func(start_index, end_index, stops)

        elif curr_command == 'Switch':
            old_string = command[1]
            new_string = command[2]
            stops = switch_func(old_string, new_string, stops)

    return f"Ready for world tour! Planned stops: {stops}"


location_stops = input()
print(word_tour(location_stops))
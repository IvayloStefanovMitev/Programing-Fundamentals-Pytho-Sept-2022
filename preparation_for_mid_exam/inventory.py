def combine_func(item, supplies):
    item1, item2 = item.split(':')

    if item1 in supplies:
        for curr_item in range(len(supplies)):
            if supplies[curr_item] == item1:

                items.insert(curr_item + 1, item2)

    return supplies


def renew_func(item, supplies):
    if item in supplies:
        items.append(item)
        items.remove(item)

    return supplies


def drop_func(item, supplies):
    if item in supplies:
        items.remove(item)

    return supplies


def collect_func(item, supplies):
    if item not in supplies:
        items.append(item)

    return supplies


def inventory(supplies):

    while True:
        command = input()
        if command == 'Craft!':
            break

        if 'Collect' in command:
            curr_command, item = command.split(' - ')
            supplies = collect_func(item, supplies)
        elif 'Drop' in command:
            curr_command, item = command.split(' - ')
            supplies = drop_func(item, supplies)
        elif 'Combine' in command:
            curr_command, item = command.split(' - ')
            supplies = combine_func(item, supplies)
        elif 'Renew' in command:
            curr_command, item = command.split(' - ')
            supplies = renew_func(item, supplies)

    result = ', '.join(item for item in supplies)
    return result


items = input().split(', ')
print(inventory(items))
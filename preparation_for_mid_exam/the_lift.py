# people = int(input())
# lift_places = input().split()
# places = []
#
# for place in lift_places:
#     places.append(int(place))
#
# all_spaces = 4 * len(places)
# free_spaces = all_spaces - sum(places)
# if free_spaces < people:
#      people_left = people - free_spaces
#      places = [4] * len(places)
#     print(f"There isn't enough space! {people_left} people in a queue!")
#     print(' '.join(str(n) for n in places))


# for all_places in range(len(places)):
#     if places[all_places] < 4:
#         places[all_places] += 4
#         people_cnt -= 4print(f"There isn't enough space! {left_people} people in a queue!")
#     print(' '.join(str(n) for n in wagons))
# if people_cnt < 0:
#     places[-1] -= abs(people_cnt)
#
#
# print(places)
# print(people_cnt)
people_waiting = int(input())
wagons = [int(n) for n in input().split()]
max_slots = 4 * len(wagons)
free_spaces = max_slots - sum(wagons)

if free_spaces < people_waiting:
    left_people = people_waiting - free_spaces
    wagons = [4] * len(wagons)
    print(f"There isn't enough space! {left_people} people in a queue!")
    print(' '.join(str(n) for n in wagons))
elif free_spaces == people_waiting:
    wagons = [4] * len(wagons)
    print(' '.join(str(n) for n in wagons))
elif free_spaces > people_waiting:
    print("The lift has empty spots!")
    wagons[0] += people_waiting
    for index in range(len(wagons)):
        if wagons[index] > 4:
            if (index + 1) < len(wagons):
                wagons[index + 1] = wagons[index] - 4
            wagons[index] = 4
    print(" ".join(str(n) for n in wagons))
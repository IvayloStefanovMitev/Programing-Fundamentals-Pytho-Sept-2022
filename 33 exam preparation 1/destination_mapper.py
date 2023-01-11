import re
destination_list = []
travel_points = 0
map_destination = input()

pattern = r'(=|\/)([A-Z][A-Za-z]{2,})\1'

result = re.findall(pattern, map_destination)


for destination in result:
    destination_list.append(destination[1])

for city in destination_list:
    travel_points += len(city)
print(f'Destinations: {", ".join(destination_list)}')
print(f'Travel Points: {travel_points}')

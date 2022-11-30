courses = {}
while True:
    command = input()
    if command == 'end':
        break

    course, name = command.split(' : ')
    if course not in courses.keys():
        courses[course] = []
    courses[course].append(name)
for course, name in courses.items():
    print(f'{course}: {len(courses[course])}')
    for curr_name in name:
        print(f'-- {curr_name}')

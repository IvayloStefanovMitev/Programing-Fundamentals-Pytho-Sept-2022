people = int(input())
capacity = int(input())

number_of_courses = people / capacity
if number_of_courses != int(number_of_courses):
    final_courses = int(number_of_courses) + 1
    print(final_courses)
else:
    print(int(number_of_courses))

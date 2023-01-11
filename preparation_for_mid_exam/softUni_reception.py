employee_one_efficiency = int(input())
employee_two_efficiency = int(input())
employee_three_efficiency = int(input())
students = int(input())
hour_counter = 0
students_counter = students
while True:
    if students_counter <= 0:
        break
    first_hour_answer = employee_one_efficiency + employee_two_efficiency + employee_three_efficiency
    hour_counter += 1
    students_counter -= first_hour_answer
    if hour_counter % 4 == 0:
        hour_counter += 1

print(f"Time needed: {hour_counter}h.")
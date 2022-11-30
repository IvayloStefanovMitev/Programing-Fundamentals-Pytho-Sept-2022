student_academy = {}
number = int(input())

for student in range(number):
    name = input()
    grade = float(input())
    if name not in student_academy.keys():
        student_academy[name] = []
    student_academy[name].append(grade)
for name, garde in student_academy.items():
    avr_grade = sum(student_academy[name]) / len(student_academy[name])
    if avr_grade >= 4.5:
        print(f'{name} -> {avr_grade:.2f}')

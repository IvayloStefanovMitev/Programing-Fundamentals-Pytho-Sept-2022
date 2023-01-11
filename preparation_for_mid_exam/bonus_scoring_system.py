from math import ceil

students = int(input())
lectures = int(input())
bonus = int(input())
max_bonus = 0
curr_attendance = 0
for student in range(1, students + 1):
    attendance = int(input())
    total_bonus = attendance / lectures * (5 + bonus)
    if total_bonus > max_bonus:
        max_bonus = total_bonus
        curr_attendance = attendance

print(f"Max Bonus: {ceil(max_bonus)}.")
print(f"The student has attended {curr_attendance} lectures.")
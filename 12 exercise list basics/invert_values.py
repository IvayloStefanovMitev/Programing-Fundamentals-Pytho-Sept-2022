numbers = input().split()
opposite_number = []
for number in numbers:
    curr_number = int(number) * -1
    opposite_number.append(curr_number)
print(opposite_number)
numbers = input().split()
number_list = []
for number in numbers:
    number_list.append(abs(float(number)))
print(number_list)
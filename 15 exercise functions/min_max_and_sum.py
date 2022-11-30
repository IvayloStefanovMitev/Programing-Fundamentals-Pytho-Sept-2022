numbers = input().split()
number_list = []
for number in numbers:
    number_list.append(int(number))
print(f"The minimum number is {min(number_list)}")
print(f"The maximum number is {max(number_list)}")
print(f"The sum number is: {sum(number_list)}")
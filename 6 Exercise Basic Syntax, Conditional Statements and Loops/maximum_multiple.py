divisor = int(input())
boundary = int(input())
curr_number = 0
for curr_number in range(boundary, divisor, -1):
    if curr_number % divisor == 0 and boundary >= curr_number > 0:
        break
print(curr_number)
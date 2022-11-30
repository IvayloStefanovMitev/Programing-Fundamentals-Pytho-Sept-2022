def perfect_number(num):
    sum_of_num = 0
    for divisors in range(1, num):
        if num % divisors == 0:
            sum_of_num += divisors
    if sum_of_num == num:
        return "We have a perfect number!"
    return "It's not so perfect."


number = int(input())
print(perfect_number(number))

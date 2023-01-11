def numbers_func(integers):
    final_lst = []
    sum_number = sum(integers)
    average_number = sum_number / len(integers)

    for number in integers:
        if number > average_number:

            final_lst.append(number)
            final_lst.sort(reverse=True)
            final_lst = final_lst[:5]

    if len(final_lst) == 0:
        return 'No'

    if len(integers) < 5:
        return'less than 5 numbers.'

    return ' '.join(str(num) for num in final_lst)


numbers = list(map(int, input().split()))
print(numbers_func(numbers))

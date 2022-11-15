lst_of_int = input().split()
lst_of_final_int = []
numbers = int(input())
for curr_int in lst_of_int:
    final_int = int(curr_int)
    lst_of_final_int.append(final_int)
for number in range(numbers):
    lst_of_final_int.remove(min(lst_of_final_int))
# print(*lst_of_final_int, sep=', ')
for i in range(len(lst_of_final_int)):
    lst_of_final_int[i] = str(lst_of_final_int[i])
print(', '.join(lst_of_final_int))




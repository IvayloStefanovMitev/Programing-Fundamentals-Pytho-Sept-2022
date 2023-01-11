number = int(input())
positive_numbers = []
negative_numbers = []
for curr_number in range(number):
    numbers = int(input())
    if numbers >= 0:
        positive_numbers.append(numbers)
    else:
        negative_numbers.append(numbers)
print(positive_numbers)
print(negative_numbers)
print(f'Count of positives: {len(positive_numbers)}')
print(f"Sum of negatives: {sum(negative_numbers)}")
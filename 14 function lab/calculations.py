def calculations(action, num1, num2):
    if action == "subtract":
        result = num1 - num2
        return result
    elif action == "add":
        result = num1 + num2
        return result
    elif action == "divide":
        result = num1 // num2
        return result
    elif action == "multiply":
        result = num1 * num2
        return result


operator = input()
first_number = int(input())
second_number = int(input())
print(calculations(operator, first_number, second_number))

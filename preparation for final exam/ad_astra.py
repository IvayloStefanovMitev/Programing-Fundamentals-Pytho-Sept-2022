import re
calories_count = 0
string = input()

pattern = r'(#|\|)([A-Za-z A-Za-z]+)\1([0-9]{2}\/[0-9]{2}\/[0-9]{2})\1([0-9]{1,5})\1'
result = re.findall(pattern, string)
for cal in result:

    curr_calories = int(cal[3])
    calories_count += curr_calories
days = int(calories_count / 2000)
print(f"You have food to last you for: {days} days!")
for database in result:
    item = database[1]
    curr_data = database[2]
    calories = int(database[3])

    print(f"Item: {item}, Best before: {curr_data}, Nutrition: {calories}")
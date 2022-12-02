import re

data = input()

pattern = r'(\d{2})([\/.-])([A-Z][a-z]{2})\2(\d{4})'
result = re.findall(pattern, data)
for curr_data in result:
    print(f"Day: {curr_data[0]}, Month: {curr_data[2]}, Year: {curr_data[3]}")

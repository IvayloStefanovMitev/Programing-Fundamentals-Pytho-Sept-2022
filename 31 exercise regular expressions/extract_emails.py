import re

emails = input()

pattern = r'\s(([a-zA-Z0-9]+[a-zA-Z0-9\.\-\_]*)@[a-z\-]+(\.[a-z]+)+)\b'

result = re.findall(pattern, emails)

for email in result:
    print(email[0])
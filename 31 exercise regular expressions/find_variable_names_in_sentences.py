import re

strings = input()

pattern = r'\b_([a-zA-Z0-9]+)\b'

result = re.findall(pattern, strings)
print(','.join(result))
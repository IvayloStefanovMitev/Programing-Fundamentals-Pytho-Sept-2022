file_name = input().split("\\")
result = file_name[-1].split(".")
print(f"File name: {result[0]}")
print(f"File extension: {result[1]}")
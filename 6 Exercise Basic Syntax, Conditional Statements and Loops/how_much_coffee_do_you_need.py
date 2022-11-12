# events = input()
# coffee_cnt = 0
# while events != 'END':
#     if events == 'coding' or events == 'CODING':
#         if events == 'CODING':
#             coffee_cnt += 2
#         else:
#             coffee_cnt += 1
#     elif events == 'dog' or events == 'DOG':
#         if events == 'DOG':
#             coffee_cnt += 2
#         else:
#             coffee_cnt += 1
#     elif events == 'cat' or events == 'CAT':
#         if events == 'CAT':
#             coffee_cnt += 2
#         else:
#             coffee_cnt += 1
#     elif events == 'movie' or events == 'MOVIE':
#         if events == 'MOVIE':
#             coffee_cnt += 2
#         else:
#             coffee_cnt += 1
#     events = input()
# if coffee_cnt > 5:
#     print("You need extra sleep")
# else:
#     print(f'{coffee_cnt}')

command = input()
cnt = 0
while command != "END":

    if command.lower() == "coding"\
            or command.lower() == "dog" or command.lower() == "cat" or command.lower() == "movie":
        if command.islower():
            cnt += 1
        else:
            cnt += 2
    command = input()
if cnt > 5:
    print("You need extra sleep")
else:
    print(f'{cnt}')


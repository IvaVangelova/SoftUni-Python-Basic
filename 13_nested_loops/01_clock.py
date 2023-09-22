# hours = 0
# minutes = 0
#
# while hours < 24:
#     minutes = 0
#     while minutes < 60:
#         print(f'{hours}:{minutes}')
#         minutes += 1
#     hours += 1

for hours in range(24):
    for minutes in range(60):
        print(f'{hours}:{minutes}')

number = int(input())
sum_1 = 0
sum_2 = 0
max_diff = 0
for i in range(number):
    first = int(input())
    second = int(input())
    if i == 0:
        sum_1 = first + second
    if i % 2 == 0:
        sum_1 = first + second
    else:
        sum_2 = first + second
    if sum_1 > sum_2 and i != 0:
        max_diff = sum_1 - sum_2
    elif sum_2 > sum_1 and i != 0:
        max_diff = sum_2 - sum_1
if max_diff == 0:
    print(f"Yes, value={sum_1}")
else:
    print(f"No, maxdiff={abs(max_diff)}")

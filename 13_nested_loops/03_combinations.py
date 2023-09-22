number = int(input())
combinations = 0

for num_1 in range(number + 1):
    for num_2 in range(number + 1):
        for num_3 in range(number + 1):
            if num_1 + num_2 + num_3 == number:
                combinations += 1
print(combinations)

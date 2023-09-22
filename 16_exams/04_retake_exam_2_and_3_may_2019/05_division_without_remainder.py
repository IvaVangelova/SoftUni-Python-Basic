numbers_count = int(input())
divide_by_2_count = 0
divide_by_3_count = 0
divide_by_4_count = 0
for num in range(numbers_count):
    number = int(input())
    if number % 2 == 0:
        divide_by_2_count += 1
    if number % 3 == 0:
        divide_by_3_count += 1
    if number % 4 == 0:
        divide_by_4_count += 1
percent_by_2 = divide_by_2_count / numbers_count * 100
percent_by_3 = divide_by_3_count / numbers_count * 100
percent_by_4 = divide_by_4_count / numbers_count * 100

print(f"{percent_by_2:.2f}%")
print(f"{percent_by_3:.2f}%")
print(f"{percent_by_4:.2f}%")

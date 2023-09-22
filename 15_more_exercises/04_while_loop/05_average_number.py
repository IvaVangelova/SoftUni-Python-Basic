number = int(input())
total = 0
average = 0
for i in range(number):
    number_2 = int(input())
    total += number_2
    average = total / number

print(f"{average:.2f}")

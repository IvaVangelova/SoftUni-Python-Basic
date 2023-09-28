number = int(input())
first_number = 0
second_number = 0
third_number = 0
forth_number = 0
first_couple = 0
second_couple = 0
total = ''

for i in range(1, 9 + 1):
    first_number = i
    for j in range(1, 9 + 1):
        second_number = j
        first_couple = i + j
        for k in range(1, 9 + 1):
            third_number = k
            for h in range(1, 9 + 1):
                forth_number = h
                second_couple = k + h
                if first_couple == second_couple:
                    if number % first_couple == 0:
                        total = str(first_number) + str(second_number) + str(third_number) + str(forth_number)
                        print(total, end=' ')

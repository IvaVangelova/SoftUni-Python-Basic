count_numbers = int(input())
even_number = 0
odd_number = 0

for numbers in range(count_numbers):
    current_number = int(input())
    if numbers % 2 == 0:
        even_number += current_number
    else:
        odd_number += current_number

if even_number == odd_number:
    print('Yes')
    print(f'Sum = {even_number}')
else:
    diff = abs(even_number - odd_number)
    print('No')
    print(f'Diff = {diff}')

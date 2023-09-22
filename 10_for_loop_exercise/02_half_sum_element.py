import sys
number = int(input())
max_number = - sys.maxsize
total = 0

for num in range(number):
    current_number = int(input())
    total += current_number
    if current_number > max_number:
        max_number = current_number
diff = total - max_number
if max_number == diff:
    print(f'Yes\nSum = {max_number}')
else:
    print(f'No\nDiff = {abs(max_number - diff)}')

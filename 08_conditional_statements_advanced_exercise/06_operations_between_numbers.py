number_1 = int(input())
number_2 = int(input())
operation = input()

result = 0

if number_1 == 0 or number_2 == 0:
    print(f'Cannot divide {number_1} by zero')
elif operation == '+':
    result = number_1 + number_2
    if result % 2 == 0:
        even_or_odd = 'even'
    else:
        even_or_odd = 'odd'
    print(f'{number_1} {operation} {number_2} = {result} - {even_or_odd}')
elif operation == '-':
    result = number_1 - number_2
    if result % 2 == 0:
        even_or_odd = 'even'
    else:
        even_or_odd = 'odd'
    print(f'{number_1} {operation} {number_2} = {result} - {even_or_odd}')
elif operation == '*':
    result = number_1 * number_2
    if result % 2 == 0:
        even_or_odd = 'even'
    else:
        even_or_odd = 'odd'
    print(f'{number_1} {operation} {number_2} = {result} - {even_or_odd}')
elif operation == '/':
    result = number_1 / number_2
    print(f'{number_1} / {number_2} = {result:.2f}')
elif operation == "%":
    result = number_1 % number_2
    print(f'{number_1} % {number_2} = {result}')

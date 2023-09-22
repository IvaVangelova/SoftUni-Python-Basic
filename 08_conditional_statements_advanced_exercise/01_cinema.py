screen_type = input()
rows = int(input())
columns = int(input())
ticket = 0

if screen_type == 'Premiere':
    ticket = 12.00
elif screen_type == 'Normal':
    ticket = 7.50
elif screen_type == 'Discount':
    ticket = 5.00

total = ticket * (rows * columns)

print(f'{total:.2f} leva')

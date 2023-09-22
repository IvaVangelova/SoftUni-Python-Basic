type_flower = input()
flower_count = int(input())
budget = int(input())

price = 0
total = 0
discount = 0
diff = 0

if type_flower == 'Roses':
    price = 5.00
    if flower_count > 80:
        discount = 0.10
elif type_flower == 'Dahlias':
    price = 3.80
    if flower_count > 90:
        discount = 0.15
elif type_flower == 'Tulips':
    price = 2.80
    if flower_count > 80:
        discount = 0.15
elif type_flower == 'Narcissus':
    price = 3.00
    if flower_count < 120:
        price *= 1.15
elif type_flower == 'Gladiolus':
    price = 2.50
    if flower_count < 80:
        price *= 1.20

total = price * flower_count * (1 - discount)

if budget - total >= 0:
    diff = budget - total
    print(f'Hey, you have a great garden with {flower_count} {type_flower} '
          f'and {diff:.2f} leva left.')
else:
    diff = total - budget
    print(f'Not enough money, you need {diff:.2f} leva more.')

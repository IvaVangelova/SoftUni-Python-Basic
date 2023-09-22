budget = int(input())
season = input()
fisherman_count = int(input())

price = 0
discount = 0
total = 0
diff = 0

if season == 'Spring':
    price = 3000
    if fisherman_count <= 6:
        discount = 0.90
    elif 7 <= fisherman_count <= 11:
        discount = 0.85
    elif fisherman_count >= 12:
        discount = 0.75
elif season == 'Summer':
    price = 4200
    if fisherman_count <= 6:
        discount = 0.90
    elif 7 <= fisherman_count <= 11:
        discount = 0.85
    elif fisherman_count >= 12:
        discount = 0.75
elif season == 'Autumn':
    price = 4200
    if fisherman_count <= 6:
        discount = 0.90
    elif 7 <= fisherman_count <= 11:
        discount = 0.85
    elif fisherman_count >= 12:
        discount = 0.75
elif season == 'Winter':
    price = 2600
    if fisherman_count <= 6:
        discount = 0.90
    elif 7 <= fisherman_count <= 11:
        discount = 0.85
    elif fisherman_count >= 12:
        discount = 0.75

total = price * discount

if (fisherman_count % 2 == 0) and not season == 'Autumn':
    total *= 0.95

if budget - total >= 0:
    diff = budget - total
    print(f'Yes! You have {diff:.2f} leva left.')
else:
    diff = total - budget
    print(f'Not enough money! You need {diff:.2f} leva.')

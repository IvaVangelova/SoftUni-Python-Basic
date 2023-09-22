budget = float(input())
season = input()

destination = ''
type_vacation = ''
diff = 0

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        type_vacation = 'Camp'
        diff = budget * 0.30
    elif season == 'winter':
        type_vacation = 'Hotel'
        diff = budget * 0.70
elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        type_vacation = 'Camp'
        diff = budget * 0.40
    elif season == 'winter':
        type_vacation = 'Hotel'
        diff = budget * 0.80
elif budget > 1000:
    destination = 'Europe'
    if season == 'summer':
        type_vacation = 'Hotel'
        diff = budget * 0.90
    elif season == 'winter':
        type_vacation = 'Hotel'
        diff = budget * 0.90

print(f'Somewhere in {destination}')
print(f'{type_vacation} - {diff:.2f}')

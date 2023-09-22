days_stay = int(input())
type_of_room = input()
rating = input()

nights = days_stay - 1
total = 0

if type_of_room == 'room for one person':
    total = nights * 18
elif type_of_room == 'apartment':
    total = nights * 25
    if days_stay < 10:
        total *= 0.70
    elif days_stay <= 15:
        total *= 0.65
    elif days_stay > 15:
        total *= 0.50
elif type_of_room == 'president apartment':
    total = nights * 35
    if days_stay < 10:
        total *= 0.90
    elif days_stay <= 15:
        total *= 0.85
    elif days_stay > 15:
        total *= 0.80

if rating == 'positive':
    total = total + (total * 0.25)
else:
    total = total - (total * 0.10)

print(f'{total:.2f}')

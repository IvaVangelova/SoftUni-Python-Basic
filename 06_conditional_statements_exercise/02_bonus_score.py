number = int(input())

LOWER_NUMBER_BONUS = 5
MEDIUM_NUMBER_BONUS = number * 0.20
LARGER_NUMBER_BONUS = number * 0.10
EXTRA_BONUS_IF_EVEN = 1
EXTRA_BONUS_IF_FIVE = 2
bonus_points = 0

if number < 100:
    bonus_points += LOWER_NUMBER_BONUS
elif number < 1000:
    bonus_points += MEDIUM_NUMBER_BONUS
else:
    bonus_points += LARGER_NUMBER_BONUS

if number % 2 == 0:
    bonus_points += EXTRA_BONUS_IF_EVEN

if number % 10 == 5:
    bonus_points += EXTRA_BONUS_IF_FIVE

total = number + bonus_points

print(bonus_points)
print(total)

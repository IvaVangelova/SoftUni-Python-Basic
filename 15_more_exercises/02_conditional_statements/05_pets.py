from math import ceil, floor

days_count = int(input())
left_food_kg = int(input())
dog_food_per_day_kg = float(input())
cat_food_per_day_kg = float(input())
turtle_food_per_day_grams = float(input())

convert_turtle_food_from_grams_to_kg = turtle_food_per_day_grams / 1000

total_dog_food = days_count * dog_food_per_day_kg
total_cat_food = days_count * cat_food_per_day_kg
total_turtle_food = days_count * convert_turtle_food_from_grams_to_kg

total_amount = total_dog_food + total_cat_food + total_turtle_food
leftover_food = left_food_kg - total_amount

if leftover_food >= 0:
    print(f'{floor(leftover_food)} kilos of food left.')

else:
    print(f"{ceil(abs(leftover_food))} more kilos of food are needed.")

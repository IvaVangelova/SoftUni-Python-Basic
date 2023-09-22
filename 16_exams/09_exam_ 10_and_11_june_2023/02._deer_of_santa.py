from math import floor,ceil
days_out = int(input())
food_kg = int(input())
first_deer_food_kg = float(input())
second_deer_food_kg = float(input())
third_deer_food_kg = float(input())

total_first = first_deer_food_kg * days_out
total_second = second_deer_food_kg * days_out
total_third = third_deer_food_kg * days_out
total = total_first + total_second + total_third

left_food = food_kg - total
if total >= food_kg:
    print(f"{ceil(abs(left_food))} more kilos of food are needed.")

else:
    print(f"{floor(left_food)} kilos of food left.")

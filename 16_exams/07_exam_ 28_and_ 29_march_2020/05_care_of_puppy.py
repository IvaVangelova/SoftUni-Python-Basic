bought_food_kg = int(input())
grams_eaten_or_adopted = input()
bought_food_grams = bought_food_kg * 1000
total_eaten = 0
is_not_enough = False
while grams_eaten_or_adopted != "Adopted":
    grams_eaten_or_adopted = int(grams_eaten_or_adopted)
    total_eaten += grams_eaten_or_adopted
    if total_eaten > bought_food_grams:
        is_not_enough = True

    grams_eaten_or_adopted = input()

if is_not_enough:
    diff = total_eaten - bought_food_grams
    print(f"Food is not enough. You need {diff} grams more.")
else:
    diff = bought_food_grams - total_eaten
    print(f"Food is enough! Leftovers: {diff} grams.")

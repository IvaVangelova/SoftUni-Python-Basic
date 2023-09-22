days_count = int(input())
total_food = float(input())

total_biscuits = 0
biscuits_eaten = 0
dog_food_total = 0
cat_food_total = 0
total_eaten_food = 0

for per_day in range(1, days_count + 1):
    dog_eat_food = int(input())
    cat_eat_food = int(input())
    dog_food_total += dog_eat_food
    cat_food_total += cat_eat_food
    total_food_per_day = dog_eat_food + cat_eat_food
    total_eaten_food += total_food_per_day
    if per_day % 3 == 0:
        biscuits_eaten = total_food_per_day * 0.10
        total_biscuits += biscuits_eaten

percent_total_eaten_food = total_eaten_food / total_food * 100
percent_eaten_food_dog = dog_food_total / total_eaten_food * 100
percent_eaten_food_cat = cat_food_total / total_eaten_food * 100

print(f"Total eaten biscuits: {round(total_biscuits)}gr.")
print(f"{percent_total_eaten_food:.2f}% of the food has been eaten.")
print(f"{percent_eaten_food_dog:.2f}% eaten from the dog.")
print(f"{percent_eaten_food_cat:.2f}% eaten from the cat.")

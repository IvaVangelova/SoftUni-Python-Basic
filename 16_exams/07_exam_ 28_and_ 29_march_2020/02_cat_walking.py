minutes_walk_per_day = int(input())
walks_per_day_count = int(input())
calories_take_per_day = int(input())

enough_walk = minutes_walk_per_day * walks_per_day_count
enough_calories = enough_walk * 5
if enough_calories >= calories_take_per_day / 2:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {enough_calories}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {enough_calories}.")

money = float(input())
gender = input()
age = int(input())
sport = input()

fitness_card = 0
if sport == "Gym":
    if gender == "m":
        fitness_card = 42
    elif gender == "f":
        fitness_card = 35
elif sport == "Boxing":
    if gender == "m":
        fitness_card = 41
    elif gender == "f":
        fitness_card = 37
elif sport == "Yoga":
    if gender == "m":
        fitness_card = 45
    elif gender == "f":
        fitness_card = 42
elif sport == "Zumba":
    if gender == "m":
        fitness_card = 34
    elif gender == "f":
        fitness_card = 31
elif sport == "Dances":
    if gender == "m":
        fitness_card = 51
    elif gender == "f":
        fitness_card = 53
elif sport == "Pilates":
    if gender == "m":
        fitness_card = 39
    elif gender == "f":
        fitness_card = 37
if age <= 19:
    fitness_card -= fitness_card * 0.20

if money >= fitness_card:
    print(f"You purchased a 1 month pass for {sport}.")
else:
    diff = abs(money - fitness_card)
    print(f"You don't have enough money! You need ${diff:.2f} more.")

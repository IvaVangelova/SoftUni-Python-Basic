people_count = int(input())
season = input()
price_person_season = 0
if people_count <= 5:
    if season == "spring":
        price_person_season = 50.00
    elif season == "summer":
        price_person_season = 48.50 * 0.85
    elif season == "autumn":
        price_person_season = 60.00
    elif season == "winter":
        price_person_season = 86.00 * 1.08
else:
    if season == "spring":
        price_person_season = 48.00
    elif season == "summer":
        price_person_season = 45.00 * 0.85
    elif season == "autumn":
        price_person_season = 49.50
    elif season == "winter":
        price_person_season = 85.00 * 1.08

total = price_person_season * people_count
print(f"{total:.2f} leva.")

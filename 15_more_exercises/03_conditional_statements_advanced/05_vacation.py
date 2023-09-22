budget = float(input())
season = input()
accommodation = ""
location = ""
price_vacation = 0
if budget <= 1000:
    accommodation = "Camp"
    if season == "Summer":
        location = "Alaska"
        price_vacation = budget * 0.65
    elif season == "Winter":
        location = "Morocco"
        price_vacation = budget * 0.45
elif budget <= 3000:
    accommodation = "Hut"
    if season == "Summer":
        location = "Alaska"
        price_vacation = budget * 0.80
    elif season == "Winter":
        location = "Morocco"
        price_vacation = budget * 0.60
elif budget > 3000:
    accommodation = "Hotel"
    if season == "Summer":
        location = "Alaska"
        price_vacation = budget * 0.90
    elif season == "Winter":
        location = "Morocco"
        price_vacation = budget * 0.90
print(f"{location} - {accommodation} - {price_vacation:.2f}")

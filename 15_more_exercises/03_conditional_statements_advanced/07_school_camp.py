season = input()
type_group = input()
students_count = int(input())
nights_count = int(input())
sport = ""
price_per_night = 0

if type_group == "boys":
    if season == "Winter":
        sport = "Judo"
        price_per_night = 9.60
    elif season == "Spring":
        sport = "Tennis"
        price_per_night = 7.20
    elif season == "Summer":
        sport = "Football"
        price_per_night = 15
elif type_group == "girls":
    if season == "Winter":
        sport = "Gymnastics"
        price_per_night = 9.60
    elif season == "Spring":
        sport = "Athletics"
        price_per_night = 7.2
    elif season == "Summer":
        sport = "Volleyball"
        price_per_night = 15
elif type_group == "mixed":
    if season == "Winter":
        sport = "Ski"
        price_per_night = 10
    elif season == "Spring":
        sport = "Cycling"
        price_per_night = 9.50
    elif season == "Summer":
        sport = "Swimming"
        price_per_night = 20

total = price_per_night * students_count * nights_count
if 20 > students_count >= 10:
    total *= 0.95
elif 50 > students_count >= 20:
    total *= 0.85
elif students_count >= 50:
    total *= 0.50

print(f"{sport} {total:.2f} lv.")

destination = input()
dates = input()
nights_count = int(input())
price_per_night = 0

if destination == "France":
    if dates == "21-23":
        price_per_night = 30
    elif dates == "24-27":
        price_per_night = 35
    elif dates == "28-31":
        price_per_night = 40
elif destination == "Italy":
    if dates == "21-23":
        price_per_night = 28
    elif dates == "24-27":
        price_per_night = 32
    elif dates == "28-31":
        price_per_night = 39
elif destination == "Germany":
    if dates == "21-23":
        price_per_night = 32
    elif dates == "24-27":
        price_per_night = 37
    elif dates == "28-31":
        price_per_night = 43

total = price_per_night * nights_count
print(f"Easter trip to {destination} : {total:.2f} leva.")

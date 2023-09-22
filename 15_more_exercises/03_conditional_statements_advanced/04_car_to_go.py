budget = float(input())
season = input()
type_car = ""
class_is = ""
price_car = 0
if budget <= 100:
    class_is = "Economy class"
    if season == "Summer":
        type_car = "Cabrio"
        price_car = budget * 0.35
    elif season == "Winter":
        type_car = "Jeep"
        price_car = budget * 0.65
elif budget <= 500:
    class_is = "Compact class"
    if season == "Summer":
        type_car = "Cabrio"
        price_car = budget * 0.45
    elif season == "Winter":
        type_car = "Jeep"
        price_car = budget * 0.80
elif budget > 500:
    class_is = "Luxury class"
    type_car = "Jeep"
    price_car = budget * 0.90
print(class_is)
print(f"{type_car} - {price_car:.2f}")

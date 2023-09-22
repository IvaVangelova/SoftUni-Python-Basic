budget = float(input())
destination = input()
season = input()
days_count = int(input())
price = 0

if season == "Winter":
    if destination == "Dubai":
        price = 45_000
    elif destination == "Sofia":
        price = 17_000
    elif destination == "London":
        price = 24_000
elif season == "Summer":
    if destination == "Dubai":
        price = 40_000
    elif destination == "Sofia":
        price = 12_500
    elif destination == "London":
        price = 20_250
total = price * days_count
if destination == "Dubai":
    total *= 0.70
elif destination == "Sofia":
    total *= 1.25
left = total - budget
if total <= budget:
    print(f"The budget for the movie is enough! We have {abs(left):.2f} leva left!")
elif total > budget:
    print(f"The director needs {left:.2f} leva more!")

budget = float(input())
liters_fuel_needed = float(input())
day_of_week = input()

total_price_fuel = liters_fuel_needed * 2.10
total = total_price_fuel + 100

if day_of_week == "Saturday":
    total *= 0.90
elif day_of_week == "Sunday":
    total *= 0.80
left_money = budget - total
if total <= budget:
    print(f"Safari time! Money left: {left_money:.2f} lv. ")
elif total > budget:
    print(f"Not enough money! Money needed: {abs(left_money):.2f} lv.")

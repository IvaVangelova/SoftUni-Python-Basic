budget = float(input())
series_count = int(input())
total = 0
for every_series in range(series_count):
    name_series = input()
    price_series = float(input())
    if name_series == "Thrones":
        price_series *= 0.50
    elif name_series == "Lucifer":
        price_series *= 0.60
    elif name_series == "Protector":
        price_series *= 0.70
    elif name_series == "TotalDrama":
        price_series *= 0.80
    elif name_series == "Area":
        price_series *= 0.90
    total += price_series
left = budget - total
if total <= budget:
    print(f"You bought all the series and left with {left:.2f} lv.")
else:
    print(f"You need {abs(left):.2f} lv. more to buy the series!")

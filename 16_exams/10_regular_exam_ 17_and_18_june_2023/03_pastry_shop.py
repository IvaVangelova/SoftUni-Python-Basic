sweet = input()
sweet_count = int(input())
day_of_month = int(input())
price = 0
if sweet == "Cake":
    if day_of_month <= 15:
        price = 24
    elif day_of_month > 15:
        price = 28.70
elif sweet == "Souffle":
    if day_of_month <= 15:
        price = 6.66
    elif day_of_month > 15:
        price = 9.80
elif sweet == "Baklava":
    if day_of_month <= 15:
        price = 12.60
    elif day_of_month > 15:
        price = 16.98

total = price * sweet_count
if day_of_month <= 22:
    if 100 <= total <= 200:
        total *= 0.85
    elif total > 200:
        total *= 0.75
    if day_of_month <= 15:
        total *= 0.90
print(f"{total:.2f}")

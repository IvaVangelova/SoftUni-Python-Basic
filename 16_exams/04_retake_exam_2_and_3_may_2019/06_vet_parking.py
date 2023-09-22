days_count = int(input())
hours_per_day_count = int(input())
total_price = 0
total_amount = 0
for day in range(1, days_count + 1):
    for hour in range(1, hours_per_day_count + 1):
        if day % 2 == 0 and hour % 2 != 0:
            total_price += 2.50
        elif day % 2 != 0 and hour % 2 == 0:
            total_price += 1.25
        else:
            total_price += 1.00
    print(f"Day: {day} - {total_price:.2f} leva")
    total_amount += total_price
    total_price = 0
print(f"Total: {total_amount:.2f} leva")

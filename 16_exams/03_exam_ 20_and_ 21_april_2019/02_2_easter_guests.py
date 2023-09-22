from math import ceil
guest_count = int(input())
budget = int(input())

cake_count = ceil(guest_count / 3)
eggs_count = guest_count * 2
cake_total = cake_count * 4.00
eggs_total = eggs_count * 0.45
total = cake_total + eggs_total

if budget >= total:
    print(f"Lyubo bought {cake_count} Easter bread and {eggs_count} eggs.")
    print(f"He has {(budget - total):.2f} lv. left.")
else:
    print("Lyubo doesn't have enough money.")
    print(f"He needs {(total - budget):.2f} lv. more.")

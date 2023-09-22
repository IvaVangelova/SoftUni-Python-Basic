from math import ceil

name_fan = input()
intended_budget = float(input())
beer_count = int(input())
chips_pack_count = int(input())

total_beer = beer_count * 1.20
price_per_pack_chips = total_beer * 0.45
total_chips = price_per_pack_chips * chips_pack_count
total_amount = total_beer + ceil(total_chips)
diff = total_amount - intended_budget

if total_amount <= intended_budget:
    print(f"{name_fan} bought a snack and has {abs(diff):.2f} leva left.")
else:
    print(f"{name_fan} needs {abs(diff):.2f} more leva!")

from math import ceil

people_count = int(input())
entrance_fee = float(input())
price_per_one_sun_lounger = float(input())
price_per_one_umbrella = float(input())

total_fee = people_count * entrance_fee
total_umbrella = (ceil(people_count / 2)) * price_per_one_umbrella
total_sun_lounger = (ceil(people_count * 0.75)) * price_per_one_sun_lounger
total_amount = total_fee + total_umbrella + total_sun_lounger
print(f"{total_amount:.2f} lv.")

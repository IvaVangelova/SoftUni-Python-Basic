chrysanthemums_count = int(input())
roses_count = int(input())
tulip_count = int(input())
season = input()
holiday_day = input()
total_chrysanthemums = 0
total_roses = 0
total_tulip = 0

if season == "Spring" or season == "Summer":
    total_chrysanthemums = chrysanthemums_count * 2.00
    total_roses = roses_count * 4.10
    total_tulip = tulip_count * 2.50
elif season == "Autumn" or season == "Winter":
    total_chrysanthemums = chrysanthemums_count * 3.75
    total_roses = roses_count * 4.50
    total_tulip = tulip_count * 4.15
total_amount = total_chrysanthemums + total_roses + total_tulip
if holiday_day == "Y":
    total_amount *= 1.15
if tulip_count > 7 and season == "Spring":
    total_amount *= 0.95
if roses_count >= 10 and season == "Winter":
    total_amount *= 0.90
total_count = chrysanthemums_count + roses_count + tulip_count
if total_count > 20:
    total_amount *= 0.80
total_amount += 2
print(f"{total_amount:.2f}")

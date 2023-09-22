months = int(input())
water = 20
internet = 15
sum_energy = 0
sum_water = 0
sum_internet = 0
sum_others = 0
for i in range(months):
    energy = float(input())
    others = (energy + water + internet) * 1.20
    sum_energy += energy
    sum_water += water
    sum_internet += internet
    sum_others += others
total_months = sum_energy + sum_water + sum_internet + sum_others
average = total_months / months
print(f"Electricity: {sum_energy:.2f} lv")
print(f"Water: {sum_water:.2f} lv")
print(f"Internet: {sum_internet:.2f} lv")
print(f"Other: {sum_others:.2f} lv")
print(f"Average: {average:.2f} lv")

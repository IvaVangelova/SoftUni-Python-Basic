trunk_capacity = float(input())
suitcase_volume = input()
total_volume_filed = 0
suitcase_count = 0
is_full = False

while suitcase_volume != "End":
    suitcase_volume = float(suitcase_volume)
    total_volume_filed += suitcase_volume
    if total_volume_filed >= trunk_capacity:
        is_full = True
        break
    suitcase_count += 1
    suitcase_volume = input()
if is_full:
    print("No more space!")
else:
    print("Congratulations! All suitcases are loaded!")

print(f"Statistic: {suitcase_count} suitcases loaded.")

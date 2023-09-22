moves = int(input())
points_10 = 0
points_20 = 0
points_30 = 0
points_40 = 0
points_50 = 0
total_points = 0
invalid = 0
for i in range(moves):
    number = int(input())
    if number < 0 or number > 50:
        total_points /= 2
        invalid += 1
    elif 0 <= number < 10:
        total_points += number * 0.20
        points_10 += 1
    elif 10 <= number < 20:
        total_points += number * 0.30
        points_20 += 1
    elif 20 <= number < 30:
        total_points += number * 0.40
        points_30 += 1
    elif 30 <= number < 40:
        total_points += 50
        points_40 += 1
    elif 40 <= number <= 50:
        total_points += 100
        points_50 += 1
percent_10 = (points_10 / moves) * 100
percent_20 = (points_20 / moves) * 100
percent_30 = (points_30 / moves) * 100
percent_40 = (points_40 / moves) * 100
percent_50 = (points_50 / moves) * 100
percent_invalid = (invalid / moves) * 100
print(f"{total_points:.2f}")
print(f"From 0 to 9: {percent_10:.2f}%")
print(f"From 10 to 19: {percent_20:.2f}%")
print(f"From 20 to 29: {percent_30:.2f}%")
print(f"From 30 to 39: {percent_40:.2f}%")
print(f"From 40 to 50: {percent_50:.2f}%")
print(f"Invalid numbers: {percent_invalid:.2f}%")

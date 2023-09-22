from math import floor

tournaments_count = int(input())
starting_points = int(input())
total_points = 0
wins = 0
for play in range(tournaments_count):
    stage = input()
    if stage == "W":
        wins += 1
        total_points += 2000
    elif stage == "F":
        total_points += 1200
    elif stage == "SF":
        total_points += 720
percent_won = (wins / tournaments_count) * 100
average = total_points / tournaments_count
total_amount = total_points + starting_points
print(f"Final points: {total_amount}")
print(f"Average points: {floor(average)}")
print(f"{percent_won:.2f}%")

first_game = input()
second_game = input()
third_game = input()
won_count = 0
lost_count = 0
drawn_count = 0

if first_game[0] > first_game[2]:
    won_count += 1
elif first_game[0] == first_game[2]:
    drawn_count += 1
elif first_game[0] < first_game[2]:
    lost_count += 1

if second_game[0] > second_game[2]:
    won_count += 1
elif second_game[0] == second_game[2]:
    drawn_count += 1
elif second_game[0] < second_game[2]:
    lost_count += 1

if third_game[0] > third_game[2]:
    won_count += 1
elif third_game[0] == third_game[2]:
    drawn_count += 1
elif third_game[0] < third_game[2]:
    lost_count += 1

print(f"Team won {won_count} games.")
print(f"Team lost {lost_count} games.")
print(f"Drawn games: {drawn_count}")

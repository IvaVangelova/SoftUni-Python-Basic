football_name = input()
matched_played = int(input())
is_zero = False
count_won = 0
count_draw = 0
count_lost = 0
if matched_played != 0:
    for i in range(matched_played):
        result = input()
        if result == "W":
            count_won += 1
        elif result == "D":
            count_draw += 1
        elif result == "L":
            count_lost += 1
    points_won = count_won * 3
    total_points = points_won + count_draw
    percent_won_games = (count_won / matched_played) * 100
    print(f"{football_name} has won {total_points} points during this season.")
    print("Total stats:")
    print(f"## W: {count_won}")
    print(f"## D: {count_draw}")
    print(f"## L: {count_lost}")
    print(f"Win rate: {percent_won_games:.2f}%")
else:
    print(f"{football_name} hasn't played any games during this season.")

tournament_name = input()
current_match_count = 0
win_match = 0
lose_match = 0
total = 0
while tournament_name != "End of tournaments":
    match_counts = int(input())
    for every_tournament in range(match_counts):
        points_desi_team = int(input())
        points_opposing_team = int(input())
        current_match_count += 1
        if points_desi_team > points_opposing_team:
            diff = points_desi_team - points_opposing_team
            win_match += 1
            total += 1
            print(f"Game {current_match_count} of tournament {tournament_name}: win with {diff} points.")
        else:
            diff = points_opposing_team - points_desi_team
            lose_match += 1
            total += 1
            print(f"Game {current_match_count} of tournament {tournament_name}: lost with {diff} points.")
    current_match_count = 0
    tournament_name = input()

if tournament_name == "End of tournaments":
    percent_win = win_match / total * 100
    percent_lose = lose_match / total * 100
    print(f"{percent_win:.2f}% matches win")
    print(f"{percent_lose:.2f}% matches lost")

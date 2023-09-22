player_name = input()
most_goals = 0
winner = ''
is_hat_trick = False
while player_name != "END":
    goals_count = int(input())
    if goals_count > most_goals:
        most_goals = goals_count
        winner = player_name
    if goals_count >= 3:
        is_hat_trick = True
    if goals_count >= 10:
        break
    last_player = winner
    player_name = input()
if player_name == "END":
    print(f"{last_player} is the best player!")
else:
    print(f"{winner} is the best player!")

if is_hat_trick:
    print(f"He has scored {most_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {most_goals} goals.")

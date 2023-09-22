days_count = int(input())
sport = input()
money_saved_per_day = 0
total_money = 0
win_count = 0
lose_count = 0
days_won = 0
days_lost = 0

for day in range(1, days_count + 1):

    while sport != "Finish":
        result = input()
        if result == "win":
            money_saved_per_day += 20
            total_money += 20
            win_count += 1
        else:
            lose_count += 1
        sport = input()
    if win_count > lose_count:
        total_money += money_saved_per_day * 0.10
        days_won += 1
    else:
        days_lost += 1
    win_count = 0
    lose_count = 0
    money_saved_per_day = 0
    if day == days_count:
        break
    sport = input()

if days_won > days_lost:
    total_money += total_money * 0.20
    print(f"You won the tournament! Total raised money: {total_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money:.2f}")

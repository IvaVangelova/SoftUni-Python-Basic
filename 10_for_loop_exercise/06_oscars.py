actor = input()
starting_points = float(input())
judges_count = int(input())
total_points = 0
total_points += starting_points

for _ in range(judges_count):
    judge_name = input()
    judge_points = float(input())
    total_points += (judge_points * len(judge_name)) / 2

    if total_points > 1250.50:
        print(f'Congratulations, {actor} got a nominee for leading role with {total_points:.1f}!')
        break

diff = 1250.50 - total_points

if total_points <= 1250.50:
    print(f'Sorry, {actor} you need {diff:.1f} more!')

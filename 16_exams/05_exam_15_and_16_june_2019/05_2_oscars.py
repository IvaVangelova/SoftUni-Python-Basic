actor_name = input()
academy_points = float(input())
judge_count = int(input())
total_points = academy_points
is_nominated = False
for i in range(judge_count):
    judge_name = input()
    judge_points = float(input())
    length_points = len(judge_name)
    points_per_judge = ((length_points * judge_points) / 2)
    total_points += points_per_judge
    if total_points >= 1250.50:
        is_nominated = True
        break


if is_nominated:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
else:
    needed_points = 1250.50 - total_points
    print(f"Sorry, {actor_name} you need {needed_points:.1f} more!")

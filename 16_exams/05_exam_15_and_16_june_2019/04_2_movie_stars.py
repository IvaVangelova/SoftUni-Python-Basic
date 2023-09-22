budget_actors = float(input())
name_or_command = input()
while name_or_command != "ACTION":
    text_length = len(name_or_command)
    if text_length <= 15:
        remuneration = float(input())
        budget_actors -= remuneration
    else:
        remuneration = budget_actors * 0.20
        budget_actors -= remuneration
    if budget_actors <= 0:
        break
    name_or_command = input()

if budget_actors > 0:
    print(f"We are left with {budget_actors:.2f} leva.")
else:
    print(f"We need {abs(budget_actors):.2f} leva for our actors.")

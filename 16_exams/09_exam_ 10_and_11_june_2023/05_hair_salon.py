goal_per_day = int(input())
command = input()
total = 0
is_achieved = False
while command != "closed":
    if command == "haircut":
        type_haircut = input()
        if type_haircut == "mens":
            total += 15
        elif type_haircut == "ladies":
            total += 20
        elif type_haircut == "kids":
            total += 10
    elif command == "color":
        type_coloring = input()
        if type_coloring == "touch up":
            total += 20
        elif type_coloring == "full color":
            total += 30
    if total >= goal_per_day:
        is_achieved = True
        break
    command = input()

if is_achieved:
    print("You have reached your target for the day!")
    print(f"Earned money: {total}lv.")
else:
    diff = goal_per_day - total
    print(f"Target not reached! You need {diff}lv. more.")
    print(f"Earned money: {total}lv.")

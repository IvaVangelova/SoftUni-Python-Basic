player_name = input()
field = input()
left_point = 301
field_points = 0
is_finish = False
success_shots = 0
unsuccessful_shots = 0
while field != "Retire":
    points = int(input())
    if field == "Single":
        field_points = points
    elif field == "Double":
        field_points = points * 2
    elif field == "Triple":
        field_points = points * 3
    if field_points == left_point:
        success_shots += 1
        is_finish = True
        break
    elif left_point - field_points < 0:
        unsuccessful_shots += 1
    else:
        success_shots += 1
        left_point -= field_points

    field = input()
if is_finish:
    print(f"{player_name} won the leg with {success_shots} shots.")
else:
    print(f"{player_name} retired after {unsuccessful_shots} unsuccessful shots.")

hall_capacity = int(input())
command_or_count_people = input()
current_people_count = 0
discount = 0
is_full = False
left_seats = hall_capacity
while command_or_count_people != "Movie time!":
    command_or_count_people = int(command_or_count_people)
    if left_seats > 0:
        if left_seats - command_or_count_people < 0:
            is_full = True
            break
        left_seats -= command_or_count_people
        if command_or_count_people % 3 == 0:
            discount += 5
    else:
        is_full = True
        break
    command_or_count_people = input()
if is_full:
    print("The cinema is full.")
elif command_or_count_people == "Movie time!":
    print(f"There are {left_seats} seats left in the cinema.")
total = (5 * (hall_capacity - left_seats)) - discount
print(f"Cinema income - {int(total)} lv.")

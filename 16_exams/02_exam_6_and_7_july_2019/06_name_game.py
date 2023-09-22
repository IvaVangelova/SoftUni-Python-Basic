name_or_command = input()
points = 0
best_points = 0
best_name = ''
while name_or_command != "Stop":
    for char in name_or_command:
        number = int(input())
        number_character = ord(char)
        if number == number_character:
            points += 10
        else:
            points += 2
        if points > best_points:
            best_points = points
            best_name = name_or_command
    if points == best_points:
        best_name = name_or_command
    points = 0
    name_or_command = input()

print(f"The winner is {best_name} with {best_points} points!")

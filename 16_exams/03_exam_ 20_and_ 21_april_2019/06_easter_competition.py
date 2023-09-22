cake_count = int(input())
point = 0
best_point = 0
best_chef = ""
for every_cake in range(cake_count):
    chef_name = input()
    command = input()
    while command != "Stop":
        grade = int(command)
        point += grade
        command = input()
    print(f"{chef_name} has {point} points.")
    if point > best_point:
        best_point = point
        best_chef = chef_name
        print(f"{best_chef} is the new number 1!")
    point = 0
print(f"{best_chef} won competition with {best_point} points!")

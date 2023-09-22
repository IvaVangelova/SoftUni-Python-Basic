name_1 = input()
name_2 = input()
num_1 = input()
points_1 = 0
points_2 = 0
while num_1 != "End of game":
    num_1 = int(num_1)
    num_2 = int(input())
    if num_1 > num_2:
        points_1 += (num_1 - num_2)
    elif num_2 > num_1:
        points_2 += (num_2 - num_1)
    elif num_1 == num_2:
        print("Number wars!")
        num_1 = int(input())
        num_2 = int(input())
        if num_1 > num_2:
            print(f"{name_1} is winner with {points_1} points")
        else:
            print(f"{name_2} is winner with {points_2} points")
        break
    num_1 = input()
if num_1 == "End of game":
    print(f"{name_1} has {points_1} points")
    print(f"{name_2} has {points_2} points")

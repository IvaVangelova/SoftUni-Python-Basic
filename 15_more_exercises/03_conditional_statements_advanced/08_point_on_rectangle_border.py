num_x1 = float(input())
num_y1 = float(input())
num_x2 = float(input())
num_y2 = float(input())
num_x = float(input())
num_y = float(input())

if num_x1 == num_x or num_x == num_x2:
    if num_y1 <= num_y <= num_y2:
        print("Border")
    else:
        print("Inside / Outside")
elif num_y1 == num_y or num_y == num_y2:
    if num_x1 <= num_x <= num_x2:
        print("Border")
    else:
        print("Inside / Outside")
else:
    print("Inside / Outside")

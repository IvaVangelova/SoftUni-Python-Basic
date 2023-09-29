start_interval = int(input())
end_interval = int(input())
one = 0
two = 0
tree = 0
four = 0
for i in range(start_interval, end_interval + 1):
    one = i
    for j in range(start_interval, end_interval + 1):
        two = j
        for k in range(start_interval, end_interval + 1):
            tree = k
            for h in range(start_interval, end_interval + 1):
                four = h
                if (one % 2 == 0 and four % 2 != 0) or (one % 2 != 0 and four % 2 == 0):
                    if (one > four) and ((two + tree) % 2 == 0):
                        number = str(one) + str(two) + str(tree) + str(four)
                        print(number, end=' ')

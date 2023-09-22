start = input()
stop = input()
for i in range(int(start[0]), int(stop[0]) + 1):
    for j in range(int(start[1]), int(stop[1]) + 1):
        for k in range(int(start[2]), int(stop[2]) + 1):
            for l in range(int(start[3]), int(stop[3]) + 1):
                if i % 2 != 0 and j % 2 != 0 and k % 2 != 0 and l % 2 != 0:
                    print(f"{i}{j}{k}{l}", end=" ")

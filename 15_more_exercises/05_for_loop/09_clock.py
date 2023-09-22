hours = 0
minutes = 0
for i in range(24):
    for j in range(60):
        print(f"{hours} : {minutes}")
        minutes += 1
    hours += 1
    minutes = 0

hours = 0
minutes = 0
seconds = 0
for i in range(24):
    for j in range(60):
        for k in range(60):
            print(f"{hours} : {minutes} : {seconds}")
            seconds += 1
        minutes += 1
        seconds = 0
    hours += 1
    minutes = 0
    

name = input()
bad_grade = 0
ear = 1
total = 0

while ear <= 12:
    grade = float(input())
    if grade < 4.00:
        bad_grade += 1
        if bad_grade > 1:
            print(f"{name} has been excluded at {ear} grade")
            break
        continue
    total += grade
    ear += 1
else:
    average = total / 12
    print(f"{name} graduated. Average grade: {average:.2f}")

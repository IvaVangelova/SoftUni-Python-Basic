students = int(input())
grade_between_2 = 0
grade_between_3 = 0
grade_between_4 = 0
grade_between_5 = 0
average_grade = 0
total_grades = 0
for every_student in range(students):
    grade = float(input())
    if 2.00 <= grade < 3.00:
        grade_between_2 += 1
    elif 3.00 <= grade < 4.00:
        grade_between_3 += 1
    elif 4.00 <= grade < 5.00:
        grade_between_4 += 1
    elif grade >= 5.00:
        grade_between_5 += 1
    total_grades += grade

percent_grade_between_2 = grade_between_2 / students * 100
percent_grade_between_3 = grade_between_3 / students * 100
percent_grade_between_4 = grade_between_4 / students * 100
percent_grade_between_5 = grade_between_5 / students * 100
percent_average_grade = total_grades / students

print(f"Top students: {percent_grade_between_5:.2f}%")
print(f"Between 4.00 and 4.99: {percent_grade_between_4:.2f}%")
print(f"Between 3.00 and 3.99: {percent_grade_between_3:.2f}%")
print(f"Fail: {percent_grade_between_2:.2f}%")
print(f"Average: {percent_average_grade:.2f}")

students_count = int(input())
top_students = 0
between_4 = 0
between_3 = 0
fail = 0
total_grades = 0
for i in range(students_count):
    exam_grade = float(input())
    if 2.00 <= exam_grade <= 2.99:
        fail += 1
    elif 3.00 <= exam_grade <= 3.99:
        between_3 += 1
    elif 4.00 <= exam_grade <= 4.99:
        between_4 += 1
    elif 5.00 <= exam_grade:
        top_students += 1
    total_grades += exam_grade
percent_top = (top_students / students_count) * 100
percent_4 = (between_4 / students_count) * 100
percent_3 = (between_3 / students_count) * 100
percent_fail = (fail / students_count) * 100
average = total_grades / students_count
print(f"Top students: {percent_top:.2f}%")
print(f"Between 4.00 and 4.99: {percent_4:.2f}%")
print(f"Between 3.00 and 3.99: {percent_3:.2f}%")
print(f"Fail: {percent_fail:.2f}%")
print(f"Average: {average:.2f}")

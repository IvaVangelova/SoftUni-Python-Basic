jury_count = int(input())
command = input()
amount = 0
total_amount = 0
total_projects = 0

while command != "Finish":

    for i in range(jury_count):
        grade = float(input())
        amount += grade
        total_amount += grade
        total_projects += 1

    avg_grade = amount / jury_count
    print(f"{command} - {avg_grade:.2f}.")
    amount = 0
    command = input()

avg_projects_grade = total_amount / total_projects
print(f"Student's final assessment is {avg_projects_grade:.2f}.")

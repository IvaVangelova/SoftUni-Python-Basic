command_or_film = input()
student_count = 0
standard_count = 0
kid_count = 0
total_ticket = 0
ticket_or_command = ""
seats = 0
amount = 0
while command_or_film != "Finish":
    free_seats_for_projection = int(input())
    ticket_or_command = input()
    seat = free_seats_for_projection
    while ticket_or_command != "End":
        if ticket_or_command == "student":
            student_count += 1
            amount += 1
        elif ticket_or_command == "standard":
            standard_count += 1
            amount += 1
        elif ticket_or_command == "kid":
            kid_count += 1
            amount += 1
        seat -= 1
        if seat <= 0:
            break
        ticket_or_command = input()

    total_ticket = student_count + standard_count + kid_count
    if seat == 0:
        total_percent = 100.00
    else:
        total_percent = (amount / free_seats_for_projection) * 100
    print(f"{command_or_film} - {total_percent:.2f}% full.")
    amount = 0
    command_or_film = input()
total_student_percent = (student_count / total_ticket) * 100
total_standard_percent = (standard_count / total_ticket) * 100
total_kid_percent = (kid_count / total_ticket) * 100

print(f"Total tickets: {total_ticket}")
print(f"{total_student_percent:.2f}% student tickets.")
print(f"{total_standard_percent:.2f}% standard tickets.")
print(f"{total_kid_percent:.2f}% kids tickets.")

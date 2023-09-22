film = input()
total_free_seats = int(input())

seat_filled = 0
student_tickets = 0
standard_tickets = 0
kids_tickets = 0
type_ticket = 0
while film != 'Finish':
    type_ticket = input()
    while type_ticket != 'End':
        seat_filled += 1
        if type_ticket == 'student':
            student_tickets += 1
        elif type_ticket == 'standard':
            standard_tickets += 1
        elif type_ticket == 'kid':
            kids_tickets += 1
        if total_free_seats == seat_filled:
            break
        type_ticket = input()
    percent_full_seats = seat_filled / total_free_seats * 100
    print(f"{film} - {percent_full_seats:.2f}% full.")
    film = input()
    if film == 'Finish':
        total_tickets = student_tickets + standard_tickets + kids_tickets
        percent_student_tickets = student_tickets / total_tickets * 100
        percent_standard_tickets = standard_tickets / total_tickets * 100
        percent_kids_tickets = kids_tickets / total_tickets * 100

        print(f"Total tickets: {total_tickets}")
        print(f"{percent_student_tickets:.2f}% student tickets.")
        print(f"{percent_standard_tickets:.2f}% standard tickets.")
        print(f"{percent_kids_tickets:.2f}% kids tickets.")
        break
    total_free_seats = int(input())
    seat_filled = 0


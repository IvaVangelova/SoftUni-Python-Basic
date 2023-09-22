stage = input()
type_ticket = input()
ticket_count = int(input())
picture_with_trophy = input()
ticket_price = 0
total = 0
is_free_tickets = True
if type_ticket == "Standard":
    if stage == "Quarter final":
        ticket_price = 55.50
    elif stage == "Semi final":
        ticket_price = 75.88
    elif stage == "Final":
        ticket_price = 110.10
elif type_ticket == "Premium":
    if stage == "Quarter final":
        ticket_price = 105.20
    elif stage == "Semi final":
        ticket_price = 125.22
    elif stage == "Final":
        ticket_price = 160.66
elif type_ticket == "VIP":
    if stage == "Quarter final":
        ticket_price = 118.90
    elif stage == "Semi final":
        ticket_price = 300.40
    elif stage == "Final":
        ticket_price = 400

total = ticket_count * ticket_price
if total > 4000:
    total *= 0.75
    is_free_tickets = False
elif total > 2500:
    total *= 0.90
if picture_with_trophy == "Y":
    if is_free_tickets:
        picture_money = ticket_count * 40
        total += picture_money
print(f"{total:.2f}")

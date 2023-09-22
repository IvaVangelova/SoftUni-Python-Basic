value_of_voucher = int(input())
command_or_purchase = input()
tickets_count = 0
other_purchased_count = 0
ticket_price = 0
while command_or_purchase != "End":
    purchase_length = len(command_or_purchase)
    if purchase_length > 8:
        ticket_price = ord(command_or_purchase[0]) + ord(command_or_purchase[1])
        if ticket_price > value_of_voucher:
            break
        tickets_count += 1
    elif purchase_length <= 8:
        ticket_price = ord(command_or_purchase[0])
        if ticket_price > value_of_voucher:
            break
        other_purchased_count += 1
    value_of_voucher -= ticket_price
    command_or_purchase = input()
print(tickets_count)
print(other_purchased_count)

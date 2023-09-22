amount_sales = int(input())
command = input()
cash = 0
card = 0
total = 0
count = 0
count_card = 0
count_cash = 0
is_cash = False
is_card = False
while command != "End":
    command = int(command)
    count += 1
    if count % 2 == 0:
        if command > 100:
            is_card = True
        elif command < 10:
            print("Error in transaction!")
        else:
            is_card = True
    else:
        if command > 100:
            print("Error in transaction!")
        elif command < 10:
            is_cash = True
        else:
            is_cash = True
    if is_card:
        card += command
        count_card += 1
        total += command
        print("Product sold!")
    elif is_cash:
        cash += command
        count_cash += 1
        total += command
        print("Product sold!")
    if total >= amount_sales:
        break
    is_cash = False
    is_card = False
    command = input()
if command == "End":
    print("Failed to collect required money for charity.")
else:
    average_cash = cash / count_cash
    average_card = card / count_card
    print(f"Average CS: {average_cash:.2f}")
    print(f"Average CC: {average_card:.2f}")

money_for_vacation = float(input())
available_cash = float(input())
days_count = 0
spend_counter = 0

while available_cash < money_for_vacation:
    type_of_action = input()
    amount_save_or_spend = float(input())
    days_count += 1
    if type_of_action == 'save':
        available_cash += amount_save_or_spend
        spend_counter = 0
    elif type_of_action == 'spend':
        available_cash -= amount_save_or_spend
        spend_counter += 1
        if spend_counter == 5:
            print("You can't save the money.")
            print(days_count)
            break
    if available_cash < 0:
        available_cash = 0
else:
    print(f'You saved the money for {days_count} days.')

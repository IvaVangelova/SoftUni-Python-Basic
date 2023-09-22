contract_term = input()
type_of_contract = input()
added_mobile_internet = input()
months_count_payment = int(input())
price_per_month = 0
if contract_term == "one":
    if type_of_contract == "Small":
        price_per_month = 9.98
    elif type_of_contract == "Middle":
        price_per_month = 18.99
    elif type_of_contract == "Large":
        price_per_month = 25.98
    elif type_of_contract == "ExtraLarge":
        price_per_month = 35.99
elif contract_term == "two":
    if type_of_contract == "Small":
        price_per_month = 8.58
    elif type_of_contract == "Middle":
        price_per_month = 17.09
    elif type_of_contract == "Large":
        price_per_month = 23.59
    elif type_of_contract == "ExtraLarge":
        price_per_month = 31.79
if added_mobile_internet == "yes":
    if price_per_month <= 10.00:
        price_per_month += 5.50
    elif price_per_month <= 30.00:
        price_per_month += 4.35
    elif price_per_month > 30.00:
        price_per_month += 3.85
total = price_per_month * months_count_payment
if contract_term == "two":
    total *= 0.9625
print(f"{total:.2f} lv.")

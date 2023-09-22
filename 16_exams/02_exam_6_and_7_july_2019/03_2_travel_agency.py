city = input()
type_package = input()
vip_discount = input()
days_stay = int(input())
price = 0
is_invalid = False

if days_stay > 7:
    days_stay -= 1
if city == "Bansko" or city == "Borovets":
    if type_package == "withEquipment":
        price = 100
        if vip_discount == "yes":
            price *= 0.90
    elif type_package == "noEquipment":
        price = 80
        if vip_discount == "yes":
            price *= 0.95
    else:
        is_invalid = True
elif city == "Varna" or city == "Burgas":
    if type_package == "withBreakfast":
        price = 130
        if vip_discount == "yes":
            price *= 0.88
    elif type_package == "noBreakfast":
        price = 100
        if vip_discount == "yes":
            price *= 0.93
    else:
        is_invalid = True
else:
    is_invalid = True
total = price * days_stay
if days_stay < 1:
    print("Days must be positive number!")
elif is_invalid is True:
    print("Invalid input!")
else:
    print(f"The price is {total:.2f}lv! Have a nice time!")

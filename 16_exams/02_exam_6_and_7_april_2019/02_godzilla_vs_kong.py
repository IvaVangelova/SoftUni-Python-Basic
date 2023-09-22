budget = float(input())
count_extra = int(input())
price_clothing_one_extra = float(input())

decor = budget * 0.10
total_clothes = count_extra * price_clothing_one_extra
if count_extra > 150:
    total_clothes *= 0.90
total_amount = total_clothes + decor
result = budget - total_amount
if total_amount > budget:
    print("Not enough money!")
    print(f"Wingard needs {abs(result):.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {result:.2f} leva left.")

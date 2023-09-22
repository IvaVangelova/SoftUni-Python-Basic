profit = float(input())
command_or_cocktail = input()
total = 0
is_acquired = False
while command_or_cocktail != "Party!":
    cocktail_price = len(command_or_cocktail)
    cocktail_count = int(input())

    sum_cocktail = cocktail_price * cocktail_count
    if sum_cocktail % 2 != 0:
        sum_cocktail *= 0.75
    total += sum_cocktail
    if total >= profit:
        is_acquired = True
        break
    command_or_cocktail = input()
if command_or_cocktail == "Party!":
    needed_money = profit - total
    print(f"We need {needed_money:.2f} leva more.")
elif is_acquired:
    print("Target acquired.")
print(f"Club income - {total:.2f} leva.")

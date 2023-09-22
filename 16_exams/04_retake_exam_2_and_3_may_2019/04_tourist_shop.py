budget = float(input())
name_product = input()
product_count = 0
total = 0
needed = 0
while name_product != "Stop":
    price_product = float(input())
    product_count += 1
    if product_count % 3 == 0:
        price_product /= 2
    if price_product > (budget - total):
        needed = price_product - (budget - total)
        break
    total += price_product
    name_product = input()
if name_product == "Stop":
    print(f"You bought {product_count} products for {total:.2f} leva.")
else:
    print("You don't have enough money!")
    print(f"You need {needed:.2f} leva!")

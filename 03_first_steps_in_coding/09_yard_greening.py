price_per_square_meter = 7.61

#18% discount from total price
qty_square_meter = float(input())
sum = price_per_square_meter * qty_square_meter
discount = sum * 0.18
total = sum - (sum * 0.18)
print(f"The final price is: {total} lv.")
print(f"The discount is: {discount} lv.")

strawberries_price = float(input())
bananas_count = float(input())
oranges_count = float(input())
raspberries_count = float(input())
strawberries_count = float(input())

raspberries_price = strawberries_price / 2
oranges_price = raspberries_price * 0.60
bananas_price = raspberries_price * 0.20

total_strawberries = strawberries_price * strawberries_count
total_bananas = bananas_price * bananas_count
total_oranges = oranges_price * oranges_count
total_raspberries = raspberries_price * raspberries_count

total_amount = total_strawberries + total_bananas + total_oranges + total_raspberries
print(f'{total_amount:.2f}')

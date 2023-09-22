annual_training_fee = int(input())

sneakers_price = annual_training_fee - (annual_training_fee * 0.40)

clothes_price = sneakers_price - (sneakers_price * 0.20)

ball_price = clothes_price * 0.25

accessories_price = ball_price * 0.20

total = annual_training_fee + sneakers_price + \
        clothes_price + ball_price + accessories_price

print(f"{total:.2f}")

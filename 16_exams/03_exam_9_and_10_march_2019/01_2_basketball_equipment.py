annual_fee = int(input())
sneakers = annual_fee * 0.60
equipment = sneakers * 0.80
ball = equipment / 4
accessories = ball / 5
total = annual_fee + sneakers + equipment + ball + accessories
print(f"{total:.2f}")


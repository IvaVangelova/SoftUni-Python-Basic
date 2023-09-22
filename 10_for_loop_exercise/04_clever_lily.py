age = int(input())
washing_machine_price = float(input())
toy_price = int(input())
money = 0
for b_day in range(1, age + 1):
    if b_day % 2 == 0:
        money += b_day * 5
        money -= 1
    else:
        money += toy_price

if money >= washing_machine_price:
    print(f'Yes! {money - washing_machine_price:.2f}')
else:
    print(f'No! {washing_machine_price - money:.2f}')

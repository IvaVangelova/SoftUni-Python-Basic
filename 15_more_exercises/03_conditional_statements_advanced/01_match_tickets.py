budget = float(input())
category = input()
people_count = int(input())
transport_cost = 0
ticket_money = 0
if category == "Normal":
    ticket_money = people_count * 249.99
elif category == "VIP":
    ticket_money = people_count * 499.99

if 1 <= people_count <= 4:
    transport_cost = budget * 0.75
elif 5 <= people_count <= 9:
    transport_cost = budget * 0.60
elif 10 <= people_count <= 24:
    transport_cost = budget * 0.50
elif 25 <= people_count <= 49:
    transport_cost = budget * 0.40
elif people_count >= 50:
    transport_cost = budget * 0.25

total = ticket_money + transport_cost
left = budget - total
if left >= 0:
    print(f"Yes! You have {left:.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(left):.2f} leva.")

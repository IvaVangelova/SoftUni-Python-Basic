budget = float(input())
nights_count = int(input())
price_per_night = float(input())
percent_extra_costs = int(input())


if nights_count > 7:
    price_per_night *= 0.95

extra_costs = percent_extra_costs / 100
total = (price_per_night * nights_count) + (budget * extra_costs)
left = budget - total
if budget >= total:
    print(f"Ivanovi will be left with {left:.2f} leva after vacation.")
else:
    print(f"{abs(left):.2f} leva needed.")


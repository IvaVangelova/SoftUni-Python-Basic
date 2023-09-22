price_luggage_over_20 = float(input())
kg_luggage = float(input())
days_trip = int(input())
luggage_count = int(input())

if kg_luggage < 10:
    price_luggage_over_20 *= 0.20
elif kg_luggage <= 20:
    price_luggage_over_20 *= 0.50
if days_trip > 30:
    price_luggage_over_20 += price_luggage_over_20 * 0.10
elif 7 <= days_trip <= 30:
    price_luggage_over_20 += price_luggage_over_20 * 0.15
elif days_trip < 7:
    price_luggage_over_20 += price_luggage_over_20 * 0.40

price_luggage = price_luggage_over_20 * luggage_count
print(f" The total price of bags is: {price_luggage:.2f} lv. ")

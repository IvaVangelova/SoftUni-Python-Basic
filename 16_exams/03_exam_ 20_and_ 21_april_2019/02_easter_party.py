guests_count = int(input())
price_per_guest = float(input())
budget = float(input())

if 10 <= guests_count <= 15:
    price_per_guest *= 0.85
elif 15 <= guests_count <= 20:
    price_per_guest *= 0.80
elif guests_count > 20:
    price_per_guest *= 0.75

cake = budget * 0.10
total = price_per_guest * guests_count + cake
diff = budget - total
if budget >= total:
    print(f"It is party time! {diff:.2f} leva left.")
else:
    print(f"No party! {abs(diff):.2f} leva needed.")

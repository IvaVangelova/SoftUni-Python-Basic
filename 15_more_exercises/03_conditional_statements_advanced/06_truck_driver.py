season = input()
kilometers_for_month = float(input())
total = 0
if kilometers_for_month <= 5000:
    if season == "Spring" or season == "Autumn":
        total = 4 * (kilometers_for_month * 0.75)
    elif season == "Summer":
        total = 4 * (kilometers_for_month * 0.90)
    elif season == "Winter":
        total = 4 * (kilometers_for_month * 1.05)
elif kilometers_for_month <= 10_000:
    if season == "Spring" or season == "Autumn":
        total = 4 * (kilometers_for_month * 0.95)
    elif season == "Summer":
        total = 4 * (kilometers_for_month * 1.10)
    elif season == "Winter":
        total = 4 * (kilometers_for_month * 1.25)
elif kilometers_for_month <= 20_000:
    total = 4 * (kilometers_for_month * 1.45)
tax = total * 0.90

print(f"{tax:.2f}")

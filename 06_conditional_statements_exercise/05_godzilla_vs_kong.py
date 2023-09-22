budget = float(input())
supernumerary_count = int(input())
price_clothes_1_supernumerary = float(input())

SET_FILM = 0.10
EXTRA_DISCOUNT_FOR_OVER_150_SUPER = 0.10

budget_set_film = budget * SET_FILM

total_supernumerary = price_clothes_1_supernumerary * supernumerary_count

if supernumerary_count >= 150:
    total_supernumerary = total_supernumerary - total_supernumerary * EXTRA_DISCOUNT_FOR_OVER_150_SUPER

expenses = total_supernumerary + budget_set_film
grand_total = budget - expenses

if grand_total < 0:
    print(f'Not enough money!')
    print(f"Wingard needs {abs(grand_total):.2f} leva more.")
else:
    print(f"Action!")
    print(f"Wingard starts filming with {grand_total:.2f} leva left.")

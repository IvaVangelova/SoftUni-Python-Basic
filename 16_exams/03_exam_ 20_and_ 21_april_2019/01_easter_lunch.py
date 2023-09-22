cake_count = int(input())
eggshells_count = int(input())
cookies_kg = int(input())

total_cakes = cake_count * 3.20
total_eggshells = eggshells_count * 4.35
total_cookies = cookies_kg * 5.40
total_paint = (eggshells_count * 12) * 0.15

total_amount = total_cakes + total_eggshells + total_cookies + total_paint
print(f"{total_amount:.2f}")

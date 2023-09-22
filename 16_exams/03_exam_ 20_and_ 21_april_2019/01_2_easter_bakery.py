flour_price_per_kg = float(input())
flour_kg = float(input())
sugar_kg = float(input())
eggshells_count = int(input())
yeast_packages = int(input())

sugar_price_per_kg = flour_price_per_kg * 0.75
eggshell_price = flour_price_per_kg * 1.10
yeast_package_price = sugar_price_per_kg * 0.20

total_flour = flour_price_per_kg * flour_kg
total_sugar = sugar_price_per_kg * sugar_kg
total_eggshells = eggshell_price * eggshells_count
total_yeast = yeast_package_price * yeast_packages

total_amount = total_flour + total_sugar + total_eggshells + total_yeast
print(f"{total_amount:.2f}")

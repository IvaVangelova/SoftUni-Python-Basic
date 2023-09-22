price_kg_vegetables = float(input())
price_kg_fruit = float(input())
total_kg_vegetables = float(input())
total_kg_fruit = float(input())

total_vegetables = price_kg_vegetables * total_kg_vegetables
total_fruit = price_kg_fruit * total_kg_fruit

bgn_to_euro = (total_vegetables + total_fruit) / 1.94

print(f"{bgn_to_euro:.2f}")

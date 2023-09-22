from math import ceil
cake_count = int(input())
max_sugar = 0
max_flour = 0
flour_spent_total = 0
sugar_spent_total = 0

for cake in range(cake_count):
    qty_sugar = int(input())
    qty_flour = int(input())
    flour_spent_total += qty_flour
    sugar_spent_total += qty_sugar
    if qty_sugar > max_sugar:
        max_sugar = qty_sugar
    if qty_flour > max_flour:
        max_flour = qty_flour
pack_sugar = ceil(sugar_spent_total / 950)
pack_flour = ceil(flour_spent_total / 750)

print(f"Sugar: {pack_sugar}")
print(f"Flour: {pack_flour}")
print(f"Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.")

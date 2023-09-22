fruit = input()
set_2_or_5 = input()
count_sets = int(input())
total = 0

if fruit == "Watermelon":
    if set_2_or_5 == "small":
        total = (2 * 56) * count_sets
    elif set_2_or_5 == "big":
        total = (5 * 28.70) * count_sets
elif fruit == "Mango":
    if set_2_or_5 == "small":
        total = (2 * 36.66) * count_sets
    elif set_2_or_5 == "big":
        total = (5 * 19.60) * count_sets
elif fruit == "Pineapple":
    if set_2_or_5 == "small":
        total = (2 * 42.10) * count_sets
    elif set_2_or_5 == "big":
        total = (5 * 24.80) * count_sets
elif fruit == "Raspberry":
    if set_2_or_5 == "small":
        total = (2 * 20) * count_sets
    elif set_2_or_5 == "big":
        total = (5 * 15.20) * count_sets

if 400 <= total <= 1000:
    total = total * 0.85
elif total > 1000:
    total = total * 0.50

print(f"{total:.2f} lv.")

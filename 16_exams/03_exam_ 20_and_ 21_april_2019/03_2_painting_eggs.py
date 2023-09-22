type_eggs = input()
color_eggs = input()
count_eggs = int(input())
price_eggs = 0

if type_eggs == "Large":
    if color_eggs == "Red":
        price_eggs = 16
    elif color_eggs == "Green":
        price_eggs = 12
    elif color_eggs == "Yellow":
        price_eggs = 9
elif type_eggs == "Medium":
    if color_eggs == "Red":
        price_eggs = 13
    elif color_eggs == "Green":
        price_eggs = 9
    elif color_eggs == "Yellow":
        price_eggs = 7
elif type_eggs == "Small":
    if color_eggs == "Red":
        price_eggs = 9
    elif color_eggs == "Green":
        price_eggs = 8
    elif color_eggs == "Yellow":
        price_eggs = 5
total = (price_eggs * count_eggs) * 0.65
print(f"{total:.2f} leva.")

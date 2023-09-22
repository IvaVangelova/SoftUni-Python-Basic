eggs_count = int(input())
red_eggs = 0
orange_eggs = 0
blue_eggs = 0
green_eggs = 0
max_colored_eggs = 0
max_color = ""

for eg in range(eggs_count):
    color_egg = input()
    if color_egg == "red":
        red_eggs += 1
        if red_eggs > max_colored_eggs:
            max_colored_eggs = red_eggs
            max_color = "red"
    elif color_egg == "orange":
        orange_eggs += 1
        if orange_eggs > max_colored_eggs:
            max_colored_eggs = orange_eggs
            max_color = "orange"
    elif color_egg == "blue":
        blue_eggs += 1
        if blue_eggs > max_colored_eggs:
            max_colored_eggs = blue_eggs
            max_color = "blue"
    elif color_egg == "green":
        green_eggs += 1
        if green_eggs > max_colored_eggs:
            max_colored_eggs = green_eggs
            max_color = "green"
print(f"Red eggs: {red_eggs}")
print(f"Orange eggs: {orange_eggs}")
print(f"Blue eggs: {blue_eggs}")
print(f"Green eggs: {green_eggs}")
print(f"Max eggs: {max_colored_eggs} -> {max_color}")

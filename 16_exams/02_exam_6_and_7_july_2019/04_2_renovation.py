from math import ceil
height_wall = int(input())
width_wall = int(input())
percent_without_paint = int(input()) / 100
command_or_liters = input()
total_meters = height_wall * width_wall * 4
without_paint = total_meters - (total_meters * percent_without_paint)
while command_or_liters != "Tired!":
    command_or_liters = int(command_or_liters)
    without_paint -= command_or_liters
    if without_paint <= 0:
        break
    command_or_liters = input()
if command_or_liters == "Tired!":
    print(f"{int(without_paint)} quadratic m left." )
elif without_paint < 0:
    print(f"All walls are painted and you have {abs(ceil(without_paint))} l paint left!")
elif without_paint == 0:
    print("All walls are painted! Great job, Pesho!")

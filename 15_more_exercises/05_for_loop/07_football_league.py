capacity_stadium = int(input())
fans_count = int(input())
sector_a = 0
sector_b = 0
sector_v = 0
sector_g = 0

for i in range(fans_count):
    sector = input()
    if sector == "A":
        sector_a += 1
    elif sector == "B":
        sector_b += 1
    elif sector == "V":
        sector_v += 1
    elif sector == "G":
        sector_g += 1

percent_a = (sector_a / fans_count) * 100
percent_b = (sector_b / fans_count) * 100
percent_v = (sector_v / fans_count) * 100
percent_g = (sector_g / fans_count) * 100
percent_fans = (fans_count / capacity_stadium) * 100

print(f"{percent_a:.2f}%")
print(f"{percent_b:.2f}%")
print(f"{percent_v:.2f}%")
print(f"{percent_g:.2f}%")
print(f"{percent_fans:.2f}%")

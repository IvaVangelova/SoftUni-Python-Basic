groups_count = int(input())
musala = 0
mont_blanc = 0
kilimanjaro = 0
k_2 = 0
everest = 0
total = 0
for clim_count in range(groups_count):
    people_in_groups_count = int(input())
    total += people_in_groups_count
    if people_in_groups_count < 6:
        musala += people_in_groups_count
    elif people_in_groups_count < 13:
        mont_blanc += people_in_groups_count
    elif people_in_groups_count < 26:
        kilimanjaro += people_in_groups_count
    elif people_in_groups_count < 41:
        k_2 += people_in_groups_count
    elif people_in_groups_count >= 41:
        everest += people_in_groups_count

percent_musala = musala / total * 100
percent_mont_blanc = mont_blanc / total * 100
percent_kilimanjaro = kilimanjaro / total * 100
percent_k_2 = k_2 / total * 100
percent_everest = everest / total * 100

print(f"{percent_musala:.2f}%")
print(f"{percent_mont_blanc:.2f}%")
print(f"{percent_kilimanjaro:.2f}%")
print(f"{percent_k_2:.2f}%")
print(f"{percent_everest:.2f}%")

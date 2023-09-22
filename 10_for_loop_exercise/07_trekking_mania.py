group_count = int(input())

mousala = 0
mont_blanc = 0
kilimanjaro = 0
k2 = 0
everest = 0

for _ in range(group_count):
    people_in_group = int(input())
    if people_in_group < 6:
        mousala += people_in_group
    elif people_in_group < 13:
        mont_blanc += people_in_group
    elif people_in_group < 26:
        kilimanjaro += people_in_group
    elif people_in_group < 41:
        k2 += people_in_group
    elif people_in_group >= 41:
        everest += people_in_group

total = mousala + mont_blanc + kilimanjaro + k2 + everest

mousala_percent = mousala / total * 100
mont_blanc_percent = mont_blanc / total * 100
kilimanjaro_percent = kilimanjaro / total * 100
k2_percent = k2 / total * 100
everest_percent = everest / total * 100

print(f'{mousala_percent:.2f}%')
print(f'{mont_blanc_percent:.2f}%')
print(f'{kilimanjaro_percent:.2f}%')
print(f'{k2_percent:.2f}%')
print(f'{everest_percent:.2f}%')

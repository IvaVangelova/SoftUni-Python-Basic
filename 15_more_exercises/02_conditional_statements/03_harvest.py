from math import floor, ceil

vineyard_square_meters = int(input())
grapes_per_square_meter = float(input())
needed_wine_liters = int(input())
workers_count = int(input())

HARVEST_WINE_PRODUCTION = vineyard_square_meters * 0.40
ONE_LITER_WINE_KG = 2.50

total_grape = HARVEST_WINE_PRODUCTION * grapes_per_square_meter
total_liters_wine = total_grape / ONE_LITER_WINE_KG
left_liters_wine = total_liters_wine - needed_wine_liters

remain_wine_per_worker = left_liters_wine / workers_count

if total_liters_wine < needed_wine_liters:

    print(f'It will be a tough winter! More {floor(abs(left_liters_wine))} liters wine needed.')

else:

    print(f'Good harvest this year! Total wine: {floor(total_liters_wine)} liters.')

    print(f'{ceil(left_liters_wine)} liters left -> {ceil(remain_wine_per_worker)} liters per person.')

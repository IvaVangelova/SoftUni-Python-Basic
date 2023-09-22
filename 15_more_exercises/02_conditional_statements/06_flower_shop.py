from math import ceil, floor

MAGNOLIAS = 3.25
HYACINTHS = 4.00
ROSES = 3.50
CACTI = 8.00

magnolias_count = int(input())
hyacinths_count = int(input())
roses_count = int(input())
cacti_count = int(input())
gift_price = float(input())

left_money = 0

total_magnolias = MAGNOLIAS * magnolias_count
total_hyacinths = HYACINTHS * hyacinths_count
total_roses = ROSES * roses_count
total_cacti = CACTI * cacti_count

total_amount = total_magnolias + total_hyacinths + total_roses + total_cacti

total_without_tax = total_amount - total_amount * 0.05
left_money = total_without_tax - gift_price

if total_without_tax >= gift_price:

    print(f'She is left with {floor(left_money)} leva.')

else:
    print(f'She will have to borrow {ceil(abs(left_money))} leva.')

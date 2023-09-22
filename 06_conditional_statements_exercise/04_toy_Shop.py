PUZZLE = 2.60
TALKING_DOLL = 3.00
TEDDY_BEAR = 4.10
MIGNON = 8.20
TRUCK = 2.00
DISCOUNT_TOTAL_SUM_50_TOYS_PERCENT = 0.25
RENT_PERCENT = 0.10

price_excursion = float(input())
puzzle_count = int(input())
talking_doll_count = int(input())
teddy_bear_count = int(input())
mignon_count = int(input())
truck_count = int(input())

money_left = 0
money_need = 0

total_qty_toys = puzzle_count + talking_doll_count + \
                 teddy_bear_count + mignon_count + truck_count

total = PUZZLE * puzzle_count + TALKING_DOLL * \
        talking_doll_count + TEDDY_BEAR * teddy_bear_count + \
        MIGNON * mignon_count + TRUCK * truck_count

if total_qty_toys >= 50:
    total = total - total * 0.25

rent_money = total * 0.10
grand_total = total - rent_money - price_excursion

if grand_total >= 0:
    print(f"Yes! {grand_total:.2f} lv left.")
else:
    print(f"Not enough money! {abs(grand_total):.2f} lv needed.")

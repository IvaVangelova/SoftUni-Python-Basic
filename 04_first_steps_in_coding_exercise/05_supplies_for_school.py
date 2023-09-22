PENS_PRICE = 5.80
MARKERS_PRICE = 7.20
DETERGENT_PRICE = 1.20

qty_pens = int(input())
qty_markers = int(input())
liter_detergent = int(input())
percent_discount = int(input()) / 100

sum_pens = PENS_PRICE * qty_pens
sum_markers = MARKERS_PRICE * qty_markers
sum_detergent = DETERGENT_PRICE * liter_detergent

sum_all = sum_pens + sum_markers + sum_detergent
discount = sum_all * percent_discount
total = sum_all - discount

print(total)

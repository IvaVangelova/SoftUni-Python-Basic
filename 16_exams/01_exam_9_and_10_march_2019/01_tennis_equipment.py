from math import ceil, floor

racket_price = float(input())
rackets_count = int(input())
sneakers_pair_count = int(input())

sneaker_price = racket_price / 6
total = racket_price * rackets_count + sneakers_pair_count * sneaker_price
other_equipment = total * 0.20
total_amount = total + other_equipment
for_payment = total_amount / 8
sponsors = total_amount - for_payment
print(f"Price to be paid by Djokovic {floor(for_payment)}")
print(f"Price to be paid by sponsors {ceil(sponsors)}")

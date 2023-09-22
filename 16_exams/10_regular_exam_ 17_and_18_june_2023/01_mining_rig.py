from math import ceil

price_video_card = int(input())
price_transition = int(input())
price_electricity_from_card_per_day = float(input())
profit_from_card_per_day = float(input())

total_cards = price_video_card * 13
total_transition = price_transition * 13
total = 1000 + total_cards + total_transition
money_per_day = profit_from_card_per_day - price_electricity_from_card_per_day
total_sum_card = money_per_day * 13
days_for_returns = total / total_sum_card
print(total)
print(ceil(days_for_returns))

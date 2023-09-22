budget = float(input())
video_cards_count = int(input())
processors_count = int(input())
ram_memory_count = int(input())

PRICE_VIDEO_CARD = 250.00
total_video_cards = video_cards_count * PRICE_VIDEO_CARD
PRICE_PROCESSOR = total_video_cards * 0.35
PRICE_RAM_MEMORY = total_video_cards * 0.10

need_money = 0
left_budget = 0

total = video_cards_count * PRICE_VIDEO_CARD + \
        processors_count * PRICE_PROCESSOR + \
        ram_memory_count * PRICE_RAM_MEMORY

if video_cards_count > processors_count:
    total = total - total * 0.15

if total > budget:
    need_money = budget - total
    print(f"Not enough money! You need {abs(need_money):.2f} leva more!")
else:
    left_budget = budget - total
    print(f"You have {left_budget:.2f} leva left!")

location_counts = int(input())
total_gold = 0
for every_location in range(location_counts):
    expected_gold_production_per_day = float(input())
    days_count_to_dig_per_location = int(input())
    for every_day in range(days_count_to_dig_per_location):
        gold_mined_for_day = float(input())
        total_gold += gold_mined_for_day
    average_gold_per_day_location = total_gold / days_count_to_dig_per_location
    if average_gold_per_day_location >= expected_gold_production_per_day:
        print(f"Good job! Average gold per day: {average_gold_per_day_location:.2f}.")
    else:
        diff = expected_gold_production_per_day - average_gold_per_day_location
        print(f"You need {diff:.2f} gold.")
    total_gold = 0

from math import floor

record_seconds = float(input())
distance_meters = float(input())
seconds_time_per_meter = float(input())

total = distance_meters * seconds_time_per_meter

delay_seconds = floor((distance_meters / 50)) * 30
amount = total + delay_seconds
diff = abs(record_seconds - amount)

if amount >= record_seconds:
    print(f"No! He was {diff:.2f} seconds slower.")
else:
    print(f" Yes! The new record is {amount:.2f} seconds.")

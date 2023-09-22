from math import floor

record_seconds = float(input())
distant_meters = float(input())
time_seconds_one_meter = float(input())
WATER_RESISTANT_EVERY_15_METERS_SECONDS = 12.50
left_seconds = 0

time_distant = distant_meters * time_seconds_one_meter

qty_time_slow = floor(distant_meters / 15)

time_seconds_slow = WATER_RESISTANT_EVERY_15_METERS_SECONDS * qty_time_slow
total_time = time_seconds_slow + time_distant

if total_time >= record_seconds:
    left_seconds = record_seconds - total_time
    print(f"No, he failed! He was {abs(left_seconds):.2f} seconds slower.")
else:
    print(f" Yes, he succeeded! The new world record is {total_time:.2f} seconds.")

minutes_control = int(input())
seconds_control = int(input())
length_chute_meters = float(input())
second_to_cover_meters = int(input())

turn_minutes_to_seconds = minutes_control * 60
total_quota_seconds = turn_minutes_to_seconds + seconds_control

lower_count = length_chute_meters / 120
lower_seconds_total = lower_count * 2.50
total_time = (length_chute_meters / 100) * second_to_cover_meters - lower_seconds_total
if total_time <= total_quota_seconds:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {total_time:.3f}.")
else:
    diff = total_time - total_quota_seconds
    print(f"No, Marin failed! He was {diff:.3f} second slower.")

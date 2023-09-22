hour = int(input())
minutes = int(input())

ADD_15_MINUTES = 15

hours_to_minutes = hour * 60
total_minutes_sum = hours_to_minutes + minutes + ADD_15_MINUTES

total_hours = total_minutes_sum // 60
total_minutes = total_minutes_sum % 60
if total_hours >= 24:
    total_hours = 0 + (total_hours - 24)

print(f'{total_hours}:{total_minutes:02d}')

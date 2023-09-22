first_competitor_seconds = int(input())
second_competitor_seconds = int(input())
third_competitor_seconds = int(input())

total_seconds = first_competitor_seconds + second_competitor_seconds + third_competitor_seconds

total_minutes = total_seconds // 60
left_seconds = total_seconds % 60

print(f'{total_minutes}:{left_seconds:02d}')

ONE_YEAR = 365
TOM_PLAY_TIME_MINUTES_PER_YEAR = 30000
PLAY_TIME_WHEN_WORK_MINUTES = 63
PLAY_TIME_WHEN_HOLIDAYS_MINUTES = 127


holiday_count = int(input())

work_days_per_year = ONE_YEAR - holiday_count

holidays_minutes_per_year = holiday_count * PLAY_TIME_WHEN_HOLIDAYS_MINUTES

work_minutes_per_year = work_days_per_year * PLAY_TIME_WHEN_WORK_MINUTES

total_minutes = holidays_minutes_per_year + work_minutes_per_year

result = TOM_PLAY_TIME_MINUTES_PER_YEAR - total_minutes
hours = abs(result) // 60
minutes = abs(result) % 60

if result < 0:
    print("Tom will run away")
    print(f'{hours} hours and {minutes} minutes more for play')
else:
    print('Tom sleeps well')
    print(f'{hours} hours and {minutes} minutes less for play')

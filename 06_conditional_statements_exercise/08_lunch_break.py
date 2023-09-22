from math import ceil

series_name = input()
episode_time = int(input())
break_time = int(input())

LUNCH_TIME = break_time / 8
RELAX_TIME = break_time / 4

total_time = episode_time + LUNCH_TIME + RELAX_TIME

time_left = break_time - total_time

if time_left >= 0:
    print(f"You have enough time to watch {series_name} and"
          f" left with {ceil(time_left)} minutes free time.")
else:
    print(f"You don't have enough time to watch {series_name}, "
          f"you need {ceil(abs(time_left))} more minutes.")

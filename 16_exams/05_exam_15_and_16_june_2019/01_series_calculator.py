from math import floor
name_serial = input()
season_count = int(input())
episodes_count = int(input())
time_episode_without_commercials = float(input())

commercials = time_episode_without_commercials * 0.20
total_time_for_episode = commercials + time_episode_without_commercials
last_episodes_time = season_count * 10
total = last_episodes_time + (total_time_for_episode * episodes_count) * season_count
print(f"Total time needed to watch the {name_serial} series is {floor(total)} minutes.")

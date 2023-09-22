from math import floor

tournament_count = int(input())
starting_points = int(input())
winner = 0
total = 0

for _ in range(tournament_count):
    stage = input()
    if stage == 'W':
        winner += 1
        total += 2000
    elif stage == 'F':
        total += 1200
    elif stage == 'SF':
        total += 720

average_point = total / tournament_count
total += starting_points
win_percent = winner / tournament_count * 100

print(f'Final points: {total}')
print(f'Average points: {floor(average_point)}')
print(f'{win_percent:.2f}%')

foot_steps = input()
total_steps = 0

while foot_steps != 'Going home':
    foot_steps = int(foot_steps)
    total_steps += foot_steps
    if total_steps >= 10_000:
        break
    foot_steps = input()
else:
    foot_steps = int(input())
    total_steps += foot_steps

if total_steps >= 10_000:
    diff = total_steps - 10_000
    print('Goal reached! Good job!')
    print(f'{diff} steps over the goal!')
else:
    diff = 10_000 - total_steps
    print(f'{diff} more steps to reach goal.')

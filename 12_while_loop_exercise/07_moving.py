width = int(input())
length = int(input())
height = int(input())
command = input()

total_space = width * length * height

while command != 'Done':
    command = int(command)
    total_space -= command
    if total_space <= 0:
        space_left = abs(total_space)
        print(f'No more free space! You need {abs(total_space)} Cubic meters more.')
        break
    command = input()
else:
    print(f'{total_space} Cubic meters left.')

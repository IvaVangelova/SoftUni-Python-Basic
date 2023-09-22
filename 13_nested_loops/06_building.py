number_of_floors = int(input())
rooms_per_floor = int(input())
type_room = ''

for current_floor in range(number_of_floors, 0, -1):
    for room_number in range(0, rooms_per_floor):
        if current_floor == number_of_floors:
            type_room = 'L'
        elif current_floor % 2 == 0:
            type_room = 'O'
        else:
            type_room = 'A'
        print(f"{type_room}{current_floor}{room_number} ", end='')
    print('')

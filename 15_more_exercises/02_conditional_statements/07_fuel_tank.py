type_fuel = input()
liter_fuel = float(input())

LIMIT_LITER_FUEL = 25

if type_fuel == 'Diesel' or type_fuel == 'Gasoline' or type_fuel == 'Gas':

    if liter_fuel >= LIMIT_LITER_FUEL:
        print(f'You have enough {type_fuel.lower()}.')
    else:
        print(f'Fill your tank with {type_fuel.lower()}!')

else:
    print('Invalid fuel!')

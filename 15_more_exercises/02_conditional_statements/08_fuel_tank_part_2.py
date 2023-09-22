GASOLINE_FOR_LITER_FUEL = 2.22
DIESEL_FOR_LITER_FUEL = 2.33
GAS_FOR_LITER_FUEL = 0.93

DISCOUNT_CARD_FOR_GASOLINE_LITER = 0.18
DISCOUNT_CARD_FOR_DIESEL_LITER = 0.12
DISCOUNT_CARD_FOR_GAS_LITER = 0.08

DISCOUNT_BETWEEN_20_25_LITERS = 0.08
DISCOUNT_ABOVE_25 = 0.10

type_fuel = input()
amount_fuel = float(input())
club_card_possession = input()

total = 0

if club_card_possession == 'Yes':

    if type_fuel == 'Gasoline':

        total = (GASOLINE_FOR_LITER_FUEL - DISCOUNT_CARD_FOR_GASOLINE_LITER) * amount_fuel

    elif type_fuel == 'Diesel':

        total = (DIESEL_FOR_LITER_FUEL - DISCOUNT_CARD_FOR_DIESEL_LITER) * amount_fuel

    elif type_fuel == 'Gas':

        total = (GAS_FOR_LITER_FUEL - DISCOUNT_CARD_FOR_GAS_LITER) * amount_fuel

else:

    if type_fuel == 'Gasoline':

        total = GASOLINE_FOR_LITER_FUEL * amount_fuel

    elif type_fuel == 'Diesel':

        total = DIESEL_FOR_LITER_FUEL * amount_fuel

    elif type_fuel == 'Gas':

        total = GAS_FOR_LITER_FUEL * amount_fuel

if 20 <= amount_fuel <= 25:

    total -= total * DISCOUNT_BETWEEN_20_25_LITERS

elif amount_fuel > 25:

    total -= total * DISCOUNT_ABOVE_25

print(f'{total:.2f} lv.')

TAXI_INITIAL_FEE = 0.70
TAXI_DAY_KM = 0.79
TAXI_NIGHT_KM = 0.90

BUSS_AT_LEAST_20_KM = 0.09
TRAIN_AT_LEAST_100_KM = 0.06

distant_km = int(input())
traveling_day_or_night = input()
total = 0

if distant_km < 20:
    if traveling_day_or_night == 'day':
        total = TAXI_INITIAL_FEE + TAXI_DAY_KM * distant_km

    elif traveling_day_or_night == 'night':
        total = TAXI_INITIAL_FEE + TAXI_NIGHT_KM * distant_km

elif distant_km < 100:
    total = distant_km * BUSS_AT_LEAST_20_KM

elif distant_km >= 100:
    total = distant_km * TRAIN_AT_LEAST_100_KM

print(f'{total:.2f}')

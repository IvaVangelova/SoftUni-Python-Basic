start_n = int(input())
stop_m = int(input())
middle_s = int(input())

for num in range(stop_m, start_n - 1, -1):
    if num % 2 == 0 and num % 3 == 0:
        if num != middle_s:
            print(f'{num}', end=" ")
        else:
            break

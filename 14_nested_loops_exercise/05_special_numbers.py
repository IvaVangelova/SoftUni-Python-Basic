number = int(input())

for num in range(1_111, 10_000):
    is_special = True
    num_as_str = str(num)
    for _, digit in enumerate(num_as_str):
        current_digit = int(digit)
        if current_digit == 0:
            is_special = False
            break
        if number % current_digit != 0:
            is_special = False
            break
    if is_special:
        print(f"{num}", end=' ')

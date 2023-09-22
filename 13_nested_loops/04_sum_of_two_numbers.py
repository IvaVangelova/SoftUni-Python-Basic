start = int(input())
finish = int(input())
magic_number = int(input())
tries = 0
is_found = False

for first_number in range(start, finish + 1):
    for second_number in range(start, finish + 1):
        tries += 1
        if first_number + second_number == magic_number:
            is_found = True
            break
    if is_found:
        break
if is_found:
    print(f'Combination N:{tries} ({first_number} + {second_number}) = {magic_number}')
else:
    print(f'{tries} combinations - neither equals {magic_number}')

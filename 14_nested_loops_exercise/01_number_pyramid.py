number = int(input())
current_number = 1
is_bigger = False
for row in range(1, number + 1):
    for col in range(1, row + 1):
        if current_number > number:
            is_bigger = True
            break
        #print(str(current_number) + " ", end='')
        print(f"{current_number} ", end='')
        current_number += 1
    if is_bigger:
        break
    print()

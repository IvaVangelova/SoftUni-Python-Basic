upper_1 = int(input())
upper_2 = int(input())
upper_3 = int(input())
is_even = True
is_even_3 = True
is_prime = True
for first in range(2, upper_1 + 1):
    if first % 2 != 0:
        is_even = False
        continue
    else:
        is_even = True
    for second in range(2, upper_2 + 1):
        for num in range(2, second):
            if second % num == 0:
                is_prime = False
                break
        else:
            is_prime = True
        for third in range(2, upper_3 + 1):
            if third % 2 != 0:
                is_even_3 = False
                continue
            else:
                is_even_3 = True
            if is_prime and is_even and is_even_3:
                print(f"{first} {second} {third}")

up_1 = int(input())
up_2 = int(input())
up_3 = int(input())

is_prime = True
for first in range(2, up_1 + 1):
    for second in range(2, up_2 + 1):
        if second == 2 or second == 3 or second == 5 or second == 7:
            is_prime = True
        else:
            is_prime = False
        # if up_2 % second == 0:  # дава грешка при 4=True
        #     is_prime = False
        for third in range(2, up_3 + 1):
            if first % 2 == 0 and third % 2 == 0 and is_prime:
                print(f"{first} {second} {third}")

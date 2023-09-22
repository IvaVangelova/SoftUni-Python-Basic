clients_count = int(input())
total = 0
average_per_person = 0
count_products = 0

for every_client in range(clients_count):
    command = input()
    while command != "Finish":
        if command == "basket":
            total += 1.50
        elif command == "wreath":
            total += 3.80
        elif command == "chocolate bunny":
            total += 7.00
        count_products += 1
        command = input()
    if count_products % 2 == 0:
        total *= 0.80
    average_per_person += total
    print(f"You purchased {count_products} items for {total:.2f} leva.")
    total = 0
    count_products = 0
average_per_person /= clients_count
print(f"Average bill per client is: {average_per_person:.2f} leva.")

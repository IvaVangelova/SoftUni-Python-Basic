eggs_in_store = int(input())
command = input()
is_sold = False
sold_eggs = 0
while command != "Close":
    count_eggs = int(input())
    if command == "Buy":
        if count_eggs > eggs_in_store:
            is_sold = True
            break
        eggs_in_store -= count_eggs
        sold_eggs += count_eggs
    elif command == "Fill":
        eggs_in_store += count_eggs
    command = input()
if is_sold:
    print("Not enough eggs in store!")
    print(f"You can buy only {eggs_in_store}.")
else:
    print("Store is closed!")
    print(f"{sold_eggs} eggs sold.")

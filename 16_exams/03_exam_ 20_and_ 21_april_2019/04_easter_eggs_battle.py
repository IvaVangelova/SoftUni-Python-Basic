eggs_first = int(input())
eggs_second = int(input())
command = input()
while command != "End":
    if command == "one":
        eggs_second -= 1
        if eggs_second == 0:
            break
    elif command == "two":
        eggs_first -= 1
        if eggs_first == 0:
            break
    command = input()
if command == "End":
    print(f"Player one has {eggs_first} eggs left.")
    print(f"Player two has {eggs_second} eggs left.")
elif eggs_second > eggs_first:
    print(f"Player one is out of eggs. Player two has {eggs_second} eggs left.")
elif eggs_first > eggs_second:
    print(f"Player two is out of eggs. Player one has {eggs_first} eggs left.")

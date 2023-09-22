bottles_detergent_count = int(input())
command = input()
total_detergent = bottles_detergent_count * 750
count_filling = 0
pots = 0
plates = 0
while command != "End":
    command = int(command)
    count_filling += 1
    if count_filling % 3 == 0:
        total_detergent -= 15 * command
        pots += command
    else:
        total_detergent -= 5 * command
        plates += command
    if total_detergent < 0:
        break
    command = input()
if total_detergent >= 0:
    print("Detergent was enough!")
    print(f"{plates} dishes and {pots} pots were washed.")
    print(f"Leftover detergent {total_detergent} ml.")
else:
    print(f"Not enough detergent, {abs(total_detergent)} ml. more necessary!")

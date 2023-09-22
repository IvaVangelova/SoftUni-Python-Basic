games_sold_count = int(input())
hearthstone = 0
fornite = 0
overwatch = 0
others = 0
for i in range(games_sold_count):
    name_game = input()
    if name_game == "Hearthstone":
        hearthstone += 1
    elif name_game == "Fornite":
        fornite += 1
    elif name_game == "Overwatch":
        overwatch += 1
    else:
        others += 1
percent_hearthstone = (hearthstone / games_sold_count) * 100
percent_fornite = (fornite / games_sold_count) * 100
percent_overwatch = (overwatch / games_sold_count) * 100
percent_others = (others / games_sold_count) * 100

print(f"Hearthstone - {percent_hearthstone:.2f}%")
print(f"Fornite - {percent_fornite:.2f}%")
print(f"Overwatch - {percent_overwatch:.2f}%")
print(f"Others - {percent_others:.2f}%")

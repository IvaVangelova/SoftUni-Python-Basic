projection = input()
movie_pack = input()
tickets_count = int(input())
price = 0
total = 0
if movie_pack == "Drink":
    if projection == "John Wick":
        price = 12
    elif projection == "Star Wars":
        price = 18
    elif projection == "Jumanji":
        price = 9
elif movie_pack == "Popcorn":
    if projection == "John Wick":
        price = 15
    elif projection == "Star Wars":
        price = 25
    elif projection == "Jumanji":
        price = 11
elif movie_pack == "Menu":
    if projection == "John Wick":
        price = 19
    elif projection == "Star Wars":
        price = 30
    elif projection == "Jumanji":
        price = 14
total = price * tickets_count
if tickets_count >= 4 and projection == "Star Wars":
    total *= 0.70
elif tickets_count == 2 and projection == "Jumanji":
    total *= 0.85

print(f"Your bill is {total:.2f} leva.")

films_count = int(input())
lower_rating = 0
lower_name = ""
upper_rating = 0
upper_name = ""
total_rating = 0
average = 0
for i in range(films_count):
    film_name = input()
    rating_film = float(input())
    total_rating += rating_film
    if lower_rating == 0 and upper_rating == 0:
        lower_rating = rating_film
        lower_name = film_name
        upper_rating = rating_film
        upper_name = film_name
    if rating_film > upper_rating:
        upper_rating = rating_film
        upper_name = film_name
    elif rating_film < lower_rating:
        lower_rating = rating_film
        lower_name = film_name
average = total_rating / films_count
print(f"{upper_name} is with highest rating: {upper_rating:.1f}")
print(f"{lower_name} is with lowest rating: {lower_rating:.1f}")
print(f"Average rating: {average:.1f}")

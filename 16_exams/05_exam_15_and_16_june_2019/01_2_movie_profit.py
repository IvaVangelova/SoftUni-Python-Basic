film_name = input()
days_count = int(input())
tickets_count = int(input())
ticket_price = float(input())
percent_for_movie = int(input())

total_per_day = ticket_price * tickets_count
total = days_count * total_per_day
percent = total * percent_for_movie / 100
profit = total - percent
print(f"The profit from the movie {film_name} is {profit:.2f} lv.")

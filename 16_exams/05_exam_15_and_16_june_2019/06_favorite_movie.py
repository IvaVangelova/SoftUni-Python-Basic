film_or_command = input()
points_per_film = 0
max_points_film = 0
best_film = ""
counter = 0
is_seven = False
while film_or_command != "STOP":
    length_current_film = len(film_or_command)
    for i in range(length_current_film):
        character = film_or_command[i]
        points_per_film += ord(character)
        if character.islower():
            points_per_film -= len(film_or_command) * 2
        elif character.isupper():
            points_per_film -= len(film_or_command)
    if points_per_film > max_points_film:
        max_points_film = points_per_film
        best_film = film_or_command
    counter += 1
    if counter == 7:
        is_seven = True
        break
    points_per_film = 0
    film_or_command = input()

if is_seven:
    print("The limit is reached.")
print(f"The best movie for you is {best_film} with {max_points_film} ASCII sum.")

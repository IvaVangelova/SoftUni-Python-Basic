from math import floor
name_or_command = input()
most_powerful_word = ""
best_points = 0
points = 0
is_vowel = False
num_length = 0
while name_or_command != "End of words":
    for i in range(len(name_or_command)):
        num_length = len(name_or_command)
        if name_or_command[0].lower() == 'a'\
                or name_or_command[0].lower() == 'e'\
                or name_or_command[0].lower() == 'i'\
                or name_or_command[0].lower() == 'o'\
                or name_or_command[0].lower() == 'u'\
                or name_or_command[0].lower() == 'y':
            is_vowel = True
        points += ord(name_or_command[i])
    if is_vowel:
        points *= num_length
    else:
        points = floor(points / num_length)
    if points > best_points:
        best_points = points
        most_powerful_word = name_or_command
    points = 0
    is_vowel = False
    name_or_command = input()
print(f"The most powerful word is {most_powerful_word} - {best_points}")

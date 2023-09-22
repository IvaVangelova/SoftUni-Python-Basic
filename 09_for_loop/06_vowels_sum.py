some_string = input()

number = 0

for character in some_string:
    if character == 'a':
        number += 1
    elif character == "e":
        number += 2
    elif character == "i":
        number += 3
    elif character == "o":
        number += 4
    elif character == "u":
        number += 5
print(number)

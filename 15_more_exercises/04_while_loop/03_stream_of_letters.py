command = input()
new_word = ""
is_found_n = False
is_found_o = False
is_found_c = False
symbol_n = 0
symbol_o = 0
symbol_c = 0
while command != "End":
    if command.isalpha():
        if command == "n":
            is_found_n = True
            symbol_n += 1
            if is_found_n and symbol_n > 1:
                new_word += command
        elif command == "o":
            is_found_o = True
            symbol_o += 1
            if is_found_o and symbol_o > 1:
                new_word += command
        elif command == "c":
            is_found_c = True
            symbol_c += 1
            if is_found_c and symbol_c > 1:
                new_word += command
        else:
            new_word += command
    if is_found_n and is_found_o and is_found_c:
        print(new_word, end=" ")
        is_found_n = False
        is_found_o = False
        is_found_c = False
        new_word = ""
        symbol_n = 0
        symbol_o = 0
        symbol_c = 0
    command = input()

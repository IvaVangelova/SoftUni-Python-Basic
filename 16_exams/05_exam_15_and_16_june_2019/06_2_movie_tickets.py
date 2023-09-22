number_a1 = int(input())
number_a2 = int(input())
number_n = int(input())
symbol_1 = ""
symbol_2 = 0
symbol_3 = 0
symbol_4 = 0
for i in range(number_a1, (number_a2 + 1) - 1):
    if i % 2 != 0:
        symbol_1 = chr(i)
        symbol_4 = i
        for j in range(1, (number_n + 1) - 1):
            symbol_2 = j
            new_n = int(number_n / 2 - 1)
            for k in range(1, new_n + 1):
                symbol_3 = k
                total = symbol_2 + symbol_3 + symbol_4
                if total % 2 != 0:
                    print(f"{symbol_1}-{symbol_2}{symbol_3}{symbol_4}")

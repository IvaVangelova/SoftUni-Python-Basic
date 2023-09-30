a = int(input())
b = int(input())
max_pass_count = int(input())
counter = 0
for i in range(35, 55 + 1):
    for j in range(64, 96 + 1):
        for k in range(49, 97 + 1):
            for m in range(49, 98 + 1):
                for n in range(64, 96 + 1):
                    for o in range(35, 55 + 1):
                        current_symbol = chr(i) + chr(j) + chr(k) + chr(m) + chr(n) + chr(o)
                        print(current_symbol, end='|')
                        counter += 1
                        if counter > max_pass_count:
                            break
                        if k == 97 and m == 98:
                            break


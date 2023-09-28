start = input()
end = input()
without = input()
combination_counter = 0
combo_start = ''
combo_middle = ''
combo_end = ''
for i in range(ord(start), ord(end) + 1):
    combo_start = chr(i)
    for j in range(ord(start), ord(end) + 1):
        combo_middle = chr(j)
        for k in range(ord(start), ord(end) + 1):
            combo_end = chr(k)
            total = combo_start + combo_middle + combo_end
            if without in total:
                continue
            print(total, end=' ')
            combination_counter += 1
print(combination_counter)

man_count = int(input())
women_count = int(input())
max_tables = int(input())
table_counter = 0
for i in range(1, man_count + 1):
    man = i
    for j in range(1, women_count + 1):
        women = j
        table_counter += 1
        if table_counter <= max_tables:
            print(f"({man} <-> {women})", end=" ")
        
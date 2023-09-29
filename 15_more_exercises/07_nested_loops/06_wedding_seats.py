last_sector = input()
first_sector_count = int(input())
seats_odd_row_count = int(input())
total_seats = 0

for i in range(65, ord(last_sector) + 1):

    for j in range(1, first_sector_count + 1):

        if j % 2 == 0:
            new_seats = seats_odd_row_count + 2
        else:
            new_seats = seats_odd_row_count

        for k in range(97, (97 + new_seats)):
            total_seats += 1
            print(f"{chr(i)}{j}{chr(k)}")

    first_sector_count += 1
    
print(total_seats)

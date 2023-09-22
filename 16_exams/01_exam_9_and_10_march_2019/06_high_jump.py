height_centimeters = int(input())
lower_bar = height_centimeters - 30
failed_bar_count = 3
height_jump = int(input())
is_failed = False
count_tries = 0
while lower_bar <= height_centimeters:
    while failed_bar_count > 0:
        count_tries += 1
        if height_jump > lower_bar:
            lower_bar += 5
            failed_bar_count = 3
            break
        else:
            failed_bar_count -= 1
            break
    if height_jump > height_centimeters and lower_bar > height_centimeters:
        break
    elif failed_bar_count <= 0:
        is_failed = True
        break
    height_jump = int(input())
if is_failed:
    print(f"Tihomir failed at {lower_bar}cm after {count_tries} jumps.")
else:
    print(f"Tihomir succeeded, he jumped over {height_centimeters}cm after {count_tries} jumps.")

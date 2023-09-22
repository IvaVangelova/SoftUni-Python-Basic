side_w = float(input())
side_h = float(input())

side_h_sm = side_h * 100
corridor = side_h_sm - 100
desk_in_row_h = corridor // 70
room_left_h = corridor - desk_in_row_h * 70

side_w_sm = side_w * 100
desk_in_row_w = side_w_sm // 120
room_left_w = side_w_sm - desk_in_row_w * 120

places = desk_in_row_h * desk_in_row_w - 3
print(int(places))


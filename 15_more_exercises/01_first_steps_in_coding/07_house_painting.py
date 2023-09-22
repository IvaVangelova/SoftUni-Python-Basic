height_x = float(input())
length_y = float(input())
height_triangular_roof_h = float(input())

cost_green_paint_liter = 3.40
cost_red_paint_liter = 4.30
front_door = 1.20 * 2
window = 1.50 * 1.50

front_side = height_x * height_x - front_door  # 33.6
back_side = height_x * height_x  # 36
left_right_side = height_x * length_y - window  # 57.75

roof_left_right_side = height_x * length_y  # 60
roof_front_back_side = (height_x * height_triangular_roof_h) / 2  # 15.6

roof_total_red_paint = (roof_left_right_side * 2 +
                        roof_front_back_side * 2) / cost_red_paint_liter  # 151.2
side_total_green = (front_side + back_side +
                    left_right_side * 2) / cost_green_paint_liter  # 185.1

print(f"{side_total_green:.2f}")
print(f"{roof_total_red_paint:.2f}")
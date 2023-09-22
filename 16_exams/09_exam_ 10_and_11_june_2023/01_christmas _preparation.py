wrapping_paper_count = int(input())
cloth_roll_count = int(input())
glue_count = float(input())
percent_discount = int(input())

sum_wrapping = wrapping_paper_count * 5.80
sum_cloth = cloth_roll_count * 7.20
sum_glue = glue_count * 1.20

total_materials = sum_wrapping + sum_cloth + sum_glue
total_with_discount = total_materials - (total_materials * percent_discount) / 100
print(f"{total_with_discount:.3f}")

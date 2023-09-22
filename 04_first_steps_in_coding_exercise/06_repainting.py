PROTECTIVE_NYLON_PER_SQUARE_METER = 1.50
PAINT_PER_LITER = 14.50
PAINT_THINNER_PER_LITER = 5.00
BAGS = 0.40

required_amount_nylon_in_sq_m = int(input())
required_amount_paint_in_liters = int(input())
amount_of_thinner_in_litrs = int(input())
hours_to_complete_work = int(input())

added_paint = required_amount_paint_in_liters + (required_amount_paint_in_liters * 0.10)
sum_paint = added_paint * PAINT_PER_LITER
added_nylon = required_amount_nylon_in_sq_m + 2
sum_nylon = added_nylon * PROTECTIVE_NYLON_PER_SQUARE_METER

sum_thinner = PAINT_THINNER_PER_LITER * amount_of_thinner_in_litrs

sum_materials = sum_paint + sum_nylon + sum_thinner + BAGS

sum_hour_work = sum_materials * 0.30
sum_workers_payment = sum_hour_work * hours_to_complete_work

total = sum_materials + sum_workers_payment

print(total)

juniors_count = int(input())
seniors_count = int(input())
type_track = input()
total_count = juniors_count + seniors_count
junior_total = 0
senior_total = 0
expenses = 0
if type_track == "trail":
    junior_total = juniors_count * 5.50
    senior_total = seniors_count * 7.00
    expenses = (junior_total + senior_total) * 0.05
elif type_track == "cross-country":
    if total_count >= 50:
        junior_total = juniors_count * (8.00 * 0.75)
        senior_total = seniors_count * (9.50 * 0.75)
        expenses = (junior_total + senior_total) * 0.05
    else:
        junior_total = juniors_count * 8.00
        senior_total = seniors_count * 9.50
        expenses = (junior_total + senior_total) * 0.05
elif type_track == "downhill":
    junior_total = juniors_count * 12.25
    senior_total = seniors_count * 13.75
    expenses = (junior_total + senior_total) * 0.05
elif type_track == "road":
    junior_total = juniors_count * 20.00
    senior_total = seniors_count * 21.50
    expenses = (junior_total + senior_total) * 0.05

total = (junior_total + senior_total) - expenses
print(f"{total:.2f}")

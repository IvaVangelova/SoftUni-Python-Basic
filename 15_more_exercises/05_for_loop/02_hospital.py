treated_patients = 0
untreated_patients = 0
doctors = 7
period = int(input())
for i in range(1, period + 1):
    patients_count_per_day = int(input())
    if i % 3 == 0:
        if untreated_patients > treated_patients:
            doctors += 1
    if patients_count_per_day > doctors:
        untreated_patients += (patients_count_per_day - doctors)
        treated_patients += doctors
    else:
        treated_patients += patients_count_per_day

print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")

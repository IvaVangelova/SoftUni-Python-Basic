loads_for_transport_count = int(input())
minibus = 0
truck = 0
train = 0
for i in range(loads_for_transport_count):
    cargo_tonnage = int(input())
    if cargo_tonnage <= 3:
        minibus += cargo_tonnage
    elif cargo_tonnage <= 11:
        truck += cargo_tonnage
    elif cargo_tonnage >= 12:
        train += cargo_tonnage
total_tons = minibus + truck + train
average_tone = ((minibus * 200) + (truck * 175) + (train * 120)) / total_tons
percent_minibus = (minibus / total_tons) * 100
percent_truck = (truck / total_tons) * 100
percent_train = (train / total_tons) * 100

print(f"{average_tone:.2f}")
print(f"{percent_minibus:.2f}%")
print(f"{percent_truck:.2f}%")
print(f"{percent_train:.2f}%")

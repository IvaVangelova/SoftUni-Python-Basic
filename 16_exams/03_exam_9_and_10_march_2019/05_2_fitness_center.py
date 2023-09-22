visitor_count = int(input())
count_back = 0
count_chest = 0
count_legs = 0
count_abs = 0
count_protein_shake = 0
count_protein_bar = 0
for every_person in range(visitor_count):
    activity_in_gym = input()
    if activity_in_gym == "Back":
        count_back += 1
    elif activity_in_gym == "Chest":
        count_chest += 1
    elif activity_in_gym == "Legs":
        count_legs += 1
    elif activity_in_gym == "Abs":
        count_abs += 1
    elif activity_in_gym == "Protein shake":
        count_protein_shake += 1
    elif activity_in_gym == "Protein bar":
        count_protein_bar += 1
total_training_people = count_back + count_chest + count_legs + count_abs
percent_training_people = (total_training_people / visitor_count) * 100
total_shopping_people = count_protein_shake + count_protein_bar
percent_shopping_people = (total_shopping_people / visitor_count) * 100
print(f"{count_back} - back")
print(f"{count_chest} - chest")
print(f"{count_legs} - legs")
print(f"{count_abs} - abs")
print(f"{count_protein_shake} - protein shake")
print(f"{count_protein_bar} - protein bar")
print(f"{percent_training_people:.2f}% - work out")
print(f"{percent_shopping_people:.2f}% - protein")

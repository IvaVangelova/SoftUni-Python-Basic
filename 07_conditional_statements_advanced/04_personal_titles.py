age = float(input())
gender = input()
type_gender = ''

if gender == 'm':
    if age >= 16:
        type_gender = 'Mr.'
    else:
        type_gender = 'Master'
else:
    if age >= 16:
        type_gender = 'Ms.'
    else:
        type_gender = 'Miss'

print(type_gender)

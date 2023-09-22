day = input()
type_day = 'Error'

if day == 'Monday':
    type_day = 'Working day'
elif day == 'Tuesday':
    type_day = 'Working day'
elif day == 'Wednesday':
    type_day = 'Working day'
elif day == 'Thursday':
    type_day = 'Working day'
elif day == 'Friday':
    type_day = 'Working day'
elif day == 'Saturday':
    type_day = 'Weekend'
elif day == 'Sunday':
    type_day = 'Weekend'

print(type_day)

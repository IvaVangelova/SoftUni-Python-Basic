exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

total_exam_minutes = (exam_hour * 60) + exam_minutes
total_arrival_minutes = (arrival_hour * 60) + arrival_minutes
diff = abs(total_exam_minutes - total_arrival_minutes)
hours = diff // 60
minutes = diff % 60

if total_arrival_minutes > total_exam_minutes:
    if hours == 0:
        print('Late')
        if diff >= 60:
            print(f'{minutes} minutes after the start')
        else:
            print(f'{diff} minutes after the start')
    elif hours != 0:
        print('Late')
        if diff >= 60:
            print(f'{hours}:{minutes:02d} hours after the start')
        else:
            print(f'{hours}:{diff:02d} hours after the start')
elif diff <= 30:
    if total_exam_minutes == total_arrival_minutes:
        print('On time')
    elif diff <= 30:
        print('On time')
        print(f'{diff} minutes before the start')
elif diff > 30:
    if hours == 0:
        print('Early')
        if diff >= 60:
            print(f'{minutes:02d} minutes before the start')
        else:
            print(f'{diff:02d} minutes before the start')
    elif hours != 0:
        print('Early')
        if diff >= 60:
            print(f'{hours}:{minutes:02d} hours before the start')
        else:
            print(f'{hours}:{diff:02d} hours before the start')

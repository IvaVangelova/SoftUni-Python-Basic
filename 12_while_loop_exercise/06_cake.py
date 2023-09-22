width = int(input())
length = int(input())

total = width * length
take = input()
while take != 'STOP':
    take = int(take)
    total -= take
    if total <= 0:
        print(f'No more cake left! You need {abs(total)} pieces more.')
        break
    take = input()
else:
    print(f'{total} pieces are left.')

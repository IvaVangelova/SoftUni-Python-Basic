animal = input()
type_group = 'unknown'

if animal == 'dog':
    type_group = 'mammal'
elif animal == 'crocodile' or animal == 'tortoise' or animal == 'snake':
    type_group = 'reptile'
print(type_group)
    
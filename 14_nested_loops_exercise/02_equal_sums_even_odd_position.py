num_1 = int(input())
num_2 = int(input())

for numbers in range(num_1, num_2 + 1):
    number_as_string = str(numbers)
    odd = 0
    even = 0
    # for index, digit in enumerate(number_as_string):
    #     if index % 2 == 0:
    #         even += int(digit)
    #     else:
    #         odd += int(digit)
    # if even == odd:
    #     print(f"{numbers} ", end='')
    for character in range(len(number_as_string)):
        digit = int(number_as_string[character])
        if character % 2 == 0:
            even += int(digit)
        else:
            odd += int(digit)
    if even == odd:
        print(f"{numbers} ", end='')

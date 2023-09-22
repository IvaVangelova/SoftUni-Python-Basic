deposit_sum = float(input())
terms_of_deposit = int(input())
annual_rate = float(input()) / 100

sum = deposit_sum + terms_of_deposit * \
((deposit_sum * annual_rate) / 12)
print(sum)

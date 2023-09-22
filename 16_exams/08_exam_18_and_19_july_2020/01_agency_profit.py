name = input()
adults_count = int(input())
kids_count = int(input())
net_price_adult = float(input())
service_fee = float(input())

adult_total = adults_count * (net_price_adult + service_fee)
kids_total = ((net_price_adult * 0.30) + service_fee) * kids_count
total_profit = adult_total + kids_total

agency_profit = total_profit * 0.20
print(f"The profit of your agency from {name} tickets is {agency_profit:.2f} lv.")

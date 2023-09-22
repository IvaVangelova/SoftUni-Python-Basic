bitcoins_count = int(input())
chinese_yuan_count = float(input())
commission = float(input())

bitcoin_to_leva = 1168
yuan_to_dollars = 0.15
dollar_to_leva = 1.76
euro_to_leva = 1.95

yuan_total_dollar = yuan_to_dollars * chinese_yuan_count
dollar_total_leva = yuan_total_dollar * dollar_to_leva
total_leva = bitcoins_count * bitcoin_to_leva + dollar_total_leva
total_to_euro = total_leva / euro_to_leva

amount_with_commission = total_to_euro - total_to_euro * (commission / 100)

print(f"{amount_with_commission:.2f}")

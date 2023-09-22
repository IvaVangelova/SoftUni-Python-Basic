price_mackerel = float(input())
price_sprat = float(input())
kg_bonito = float(input())
kg_safrid = float(input())
kg_mussels = int(input())

MUSSELS_PRICE = 7.50
BONITO_PRICE = price_mackerel + price_mackerel * 0.60
SAFRID_PRICE = price_sprat + price_sprat * 0.80

bonito_sum = kg_bonito * BONITO_PRICE
safrid_sum = kg_safrid * SAFRID_PRICE
mussels_sum = kg_mussels * MUSSELS_PRICE

total = bonito_sum + safrid_sum + mussels_sum

print(f'{total:.2f}')


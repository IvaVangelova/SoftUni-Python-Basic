CHICKEN_MENU = 10.35
FISH_MENU = 12.40
VEGETERIAN_MENU = 8.15
DELIVERY = 2.50

qty_chichen_menu = int(input())
qty_fish_menu = int(input())
qty_vegeterian_menu = int(input())

sum = CHICKEN_MENU * qty_chichen_menu + \
      FISH_MENU * qty_fish_menu + \
      VEGETERIAN_MENU * qty_vegeterian_menu
desert = sum * 0.20
total = sum + desert + DELIVERY

print(f"{total:.2f}")

qty_pages = int(input())
pages_for_hour = int(input())
qty_days = int(input())

need_hours = qty_pages // pages_for_hour
need_days = need_hours // qty_days

print(need_days)

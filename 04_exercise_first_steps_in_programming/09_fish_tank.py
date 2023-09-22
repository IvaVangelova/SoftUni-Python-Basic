length = int(input())
width = int(input())
height = int(input())
percent = int(input()) / 100

total = ((length * width * height) / 1000)
total_all = total - (total * percent)

print(total_all)

rent = int(input())
statuettes = rent * 0.70
catering = statuettes * 0.85
voiceover = catering / 2

total = rent + statuettes + catering + voiceover
print(f"{total:.2f}")

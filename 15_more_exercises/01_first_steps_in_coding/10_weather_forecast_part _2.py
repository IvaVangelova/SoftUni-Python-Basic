degrees = float(input())

if degrees >= 26.00 and degrees <= 35.00:
    print("Hot")
elif degrees >= 20.10 and degrees <= 25.90:
    print("Warm")
elif degrees >= 15.00 and degrees <= 20.00:
    print("Mild")
elif degrees >= 12.00 and degrees <= 14.90:
    print("Cool")
elif degrees >= 5.00 and degrees <= 11.90:
    print("Cold")
else:
    print("unknown")

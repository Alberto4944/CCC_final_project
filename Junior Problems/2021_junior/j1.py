# Completed on 5/16/2025

boiling_temp = int(input())

pressure = (boiling_temp * 5) - 400
print(pressure)
if pressure < 100:
    print("1")
elif pressure > 100:
    print("-1")
else:
    print("0")
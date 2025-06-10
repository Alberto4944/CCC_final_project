# Completed on 5/19/2025

peppers = int(input())
scoville = 0

for pepper in range(peppers):
    pepper = input()
    if pepper[0] == "P":
        scoville+=1500
    elif pepper[0] == "M":
        scoville+=6000
    elif pepper[0] == "S":
        scoville+=15500
    elif pepper[0] == "C":
        scoville+=40000
    elif pepper[0] == "T":
        scoville+=75000
    else:
        scoville+=125000

print(scoville)
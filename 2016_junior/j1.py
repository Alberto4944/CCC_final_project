# Completed on 5/22/2025

wins = 0

for games in range(6):
    result = input()
    if result == "W":
        wins+=1
        
if wins > 4:
    print("1")
elif wins > 2:
    print("2")
elif wins > 0:
    print("3")
else:
    print("-1")
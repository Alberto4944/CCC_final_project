scoreA = 0
scoreB = 0

for score in [3,2,1]:
    scoreA = int(input()) * score + scoreA
    
for score in [3,2,1]:
    scoreB = int(input()) * score + scoreB
    
if scoreA > scoreB:
    print("A")
elif scoreB > scoreA:
    print("B")
else:
    print("T")
goal = int(input())
infected = int(input())
spread = int(input())
day = 0

while infected < goal:
    day+=1
    for i in range(infected):
        infected = infected + spread**day
    print(infected)
    
    
    
print(day)
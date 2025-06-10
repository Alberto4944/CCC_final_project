# Completed on 6/3/2025

goal = int(input())
infected = int(input())
spread = int(input())

day = 0
active = 0
active = infected

while infected <= goal:
    active = active * spread
    infected+=active
    day+=1

print(day)
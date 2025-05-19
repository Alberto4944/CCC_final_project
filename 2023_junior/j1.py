# Completed on 5/19/2025

packages = int(input())
collisions = int(input())

score = (50 * packages) - (10 * collisions)

if packages > collisions:
    score+=500
    
print(score)
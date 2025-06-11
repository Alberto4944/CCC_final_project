# Completed on 6/11/2025

people = int(input())
hats = []
output = 0

for person in range(people):
    number = int(input())
    hats.append(number)
    
for person in range(people//2):
    if hats[person] == hats[people//2+person]:
        output+=2
                
print(output)
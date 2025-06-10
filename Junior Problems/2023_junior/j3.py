# Completed on 6/10/2025

people = int(input())

days = {1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0}

for person in range(people):
    avaliablility = input()
    for letter in range(len(avaliablility)):
        if avaliablility[letter] == "Y":
            days[letter+1]+=1

largest_days = []
for i in range(1,6):
    if days[i] == max(days.values()):
        largest_days.append(str(i))
     
print(",".join(largest_days))
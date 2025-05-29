# Almost completed on 5/29/2025, but not finished if they are equal and CCC grader is down until 5/30

people = int(input())
avaliablility = [0, 0, 0, 0, 0]
highest = 0

for person in range(people):
    avaliable = input()
    for i in range(4):
        if avaliable[i] == "Y":
            avaliablility[i]+=1
        if avaliablility[i] > highest:
            highest = i + 1  
            
print(highest)
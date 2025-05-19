people = int(input())
day1 = 0
day2 = 0
day3 = 0
day4 = 0
day5 = 0

for i in range(people):
    avaliablility = input()
    
    for a in avaliablility:
        if a == "Y":
            if a == avaliablility[0]:
                day1+=1
            elif a == avaliablility[1]:
                day2+=1
            elif a == avaliablility[2]:
                day3+=1
            elif a == avaliablility[3]:
                day4+=1
            else:
                day5+=1

most = day1
for value in [day1, day2, day3, day4, day5]:
    if value > most:
        most = value
        print(most)
# Completed on 4/28/2025

parking_spaces = int(input())
yesterday = input()
today = input()

yesterday_list = []
today_list = []
occupied = 0

for status in yesterday:
    yesterday_list.append(status)
for status in today:
    today_list.append(status)
    
for i in range(parking_spaces):
    if yesterday[i] == "C" and today[i] == "C":
        occupied+=1
        
print(occupied)
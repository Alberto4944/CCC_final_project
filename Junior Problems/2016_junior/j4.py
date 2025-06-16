# Completed on 6/13/2025

time = input().split(":")
hour = int(time[0])
minute = int(time[1])

total_distance = 0
   
while total_distance < 120:
    minute+=10 # 10 Minutes IRL
    if hour >= 7 and hour < 10 or hour >= 15 and hour < 19: 
        total_distance+=5 # Half Distance in 10 mins
    else:
        total_distance+=10 # Regular Distance in 10 mins
    if minute >= 60: # If the minutes go past 60
        hour+=1
        minute = minute - 60
    if hour >= 24: # If the new day starts
        hour = hour - 24

# Check if the numbers are missing the placeholder 0 in the beginning
if len(str(hour)) == 1:
    hour = f"0{hour}"
if len(str(minute)) == 1:
    minute = f"0{minute}"

print(f"{hour}:{minute}")
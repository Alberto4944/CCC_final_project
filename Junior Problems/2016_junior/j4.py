time = input().split(":")
hour = int(time[0])
minute = int(time[1])

total_minutes = 0

def convert_to_time(hour, minute):
    if len(hour) == 1:
        hour == 
def update_hour(hour, minute):
    if minute == 60:
        minute = 0
        return [hour+1, minute]
    return [hour, minute]

while total_minutes < 120:
    #if hour < 15 and hour > 10 or hour < 7 or hour > 19:
    total_minutes+=20
    minute+=20
    update = update_hour(hour, minute)
    hour = update[0]
    minute = update[1]
    
print(total_minutes)
print(f"{hour}:{minute}")
# Completed 5/16/2025

number = " "
direction = " "
previous_direction = " "
steps = 0

while number != "99999":
    number = str(input())
    if number != "99999":
        if (int(number[0]) + int(number[1])) % 2:
            direction = "left"
            previous_direction = direction
        elif (int(number[0]) + int(number[1])) == 0:
            direction = previous_direction
        else:
            direction = "right"
            previous_direction = direction
        
        steps = int(number) - (int(number[0]) * 10000) - (int(number[1]) * 1000)
        print(f"{direction} {steps}")
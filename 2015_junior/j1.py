# Completed on 6/2/2025 and tested with two cases. CCC Grader is still down.

month = int(input())
day = int(input())

if month >= 2:
    if month == 2 and day == 18:
        print("Special")
    else:
        print("After")
else:
    print("Before")
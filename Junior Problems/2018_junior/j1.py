# Completed on 4/28/2025

list = []

for i in range(4):
    number = int(input())
    list.append(number)

if list[0] == 9 or list[0] == 8:
    if list[3] == 8 or list[3] == 9:
        if list[1] == list[2]:
            print("ignore")
        else:
            print("answer")
    else:
        print("answer")
else:
    print("answer")
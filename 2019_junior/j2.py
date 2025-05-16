lines = int(input())
for line in range(lines):
    num = input().split(" ")
    times = int(num[0])
    for i in range(times):
        print(num[1],end="")
    print("")
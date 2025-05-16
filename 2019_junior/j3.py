lines = int(input())
times = []

for line in range(lines):
    seq = input()
    for i in seq:
        if len(times) > 0 and i != times[-1]:
            print(f"{len(times)} {times[0]}",end=" ")
            times.clear()
        times.append(i)
    print(f"{len(times)} {times[0]}")
    times.clear()
# Completed on 6/3/2025

x = []
y = []

drops = int(input())

for drop in range(drops):
    coords = input()
    for char in range(len(coords)):
        if coords[char] == ",":
            x.append(int(coords[:char]))
            y.append(int(coords[char+1:]))
x.sort()
y.sort()

print(f"{x[0]-1},{y[0]-1}")
print(f"{x[-1]+1},{y[-1]+1}")
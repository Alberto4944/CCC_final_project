distances = "3 10 12 5".split() # input().split()
for num in range(len(distances)):
    distances[num] = int(distances[num])

total_distance = distances[-1]
first_row = []
print(distances)
for i in range(5):
    print(sum(distances[0:i]))
    first_row.append(sum(distances[0:i]))
print(first_row)
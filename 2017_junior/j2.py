# Completed on 6/2/2025

original = int(input())
shifts = int(input())
result = 0
for i in range(shifts + 1):
    result = result + (original * (10 ** i))
print(result)
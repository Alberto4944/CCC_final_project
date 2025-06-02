# Completed on 6/2/2025 and tested with two cases. CCC Grader is still down.

original = int(input())
shifts = int(input())
result = 0
for i in range(shifts + 1):
    result = result + (original * (10 ** i))
    print(result)
print(result)
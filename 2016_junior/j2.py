# Completed on 6/4/2025

square = []
magic = True

for row in range(4):
    nums = input().split()
    square.append(nums)

first_sum = 0
for number in square[0]:
    first_sum+=int(number)

def find_sums(square):
    for row in range(1,4):
        sum_ = 0
        for number in square[row]:
            sum_+=int(number)
        if sum_ != first_sum:
            return "not magic"
        
    for col in range(4):
        sum__ = 0
        for row in range(4):
            sum__+=int(square[row][col])
        if sum__ != first_sum:
            return "not magic"
    return "magic"

print(find_sums(square))
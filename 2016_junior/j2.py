row_1 = input().split()
row_2 = input().split()
row_3 = input().split()
row_4 = input().split()
row_sum = 0
rows_good = True
col_sum = 0

for i in [row_1, row_2, row_3, row_4]:
    previous_row_sum = row_sum
    for value in i:
        row_sum+=value
    if previous_row_sum != row_sum:
        rows_good = False
    
if rows_good == True:
    for i in range(4):
        for value in [row_1, row_2, row_3, row_4]:
            col_sum+=value
            
if row_sum == col_sum:
    print("magic")
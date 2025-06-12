# Completed on 6/12/2025

collumns = int(input())
row1 = input().split()
row2 = input().split()

tape = (row1.count("1") + row2.count("1")) * 3
          
def check_left_right(row, triangle, tape):
    if row[triangle-1] == "1" and triangle > 0:
        tape-=1
    if triangle < (collumns-1) and row[triangle+1] == "1":
        tape-=1
    return tape          

for triangle in range(collumns):
    if row1[triangle] == "1":
        if triangle % 2 == 0 and row2[triangle] == "1":
            tape-=1
        tape = check_left_right(row1, triangle, tape)
    if row2[triangle] == "1":
        if triangle % 2 == 0 and row1[triangle] == "1":
            tape-=1
        tape = check_left_right(row2, triangle, tape)
        
print(tape)
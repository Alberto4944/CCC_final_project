collumns = 5#int(input())

row1 = "1 0 1 0 1".split()#input().split()
row2 = "0 0 0 0 0".split()#input().split()

tape = (row1.count("1") + row2.count("1")) * 3



for triangle in range(len(row1)):
    if row1[triangle] == "1":
        if row1[triangle+1] == "1" and triangle < len(row1)-1 or row1[triangle-1] == "1" and triangle > 0 == "1" or row2[triangle] == "1":
            tape-=1

print(tape)

print(row1, row2)
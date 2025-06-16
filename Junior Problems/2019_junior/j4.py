# Completed on 5/15/2025

grid = [1,2,3,4]
hold1 = 0
hold2 = 0
times = input()

# Basically swaps everything
for i in times:
    if i == "H":
        hold1 = grid[0]
        hold2 = grid[1]
        grid[0] = grid[2]
        grid[2] = hold1
        grid[1] = grid[3]
        grid[3] = hold2
    else:
        hold1 = grid[0]
        hold2 = grid[2]
        grid[0] = grid[1]
        grid[1] = hold1
        grid[2] = grid[3]
        grid[3] = hold2
        
print(f"""{grid[0]} {grid[1]}
{grid[2]} {grid[3]}""")
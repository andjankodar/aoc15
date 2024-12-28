import copy
input = open("aoc_15_18_1\\input.txt").read()
grid = [list(line) for line in input.splitlines()]
directions = {(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)}

for i in range(0, 100):
    nextState = copy.deepcopy(grid)

    for j in range(0,len(grid)):
        for k in range(0, len(grid[0])):
            on = 0
            for dir in directions:
                dr = dir[0]
                dc = dir[1]

                if j + dr >= 0 and j + dr < len(grid) and k + dc >= 0 and k + dc < len(grid[0]):
                    if grid[j+dr][k+dc] == '#':
                        on+=1
            
            if grid[j][k] == '.' and on == 3:
                nextState[j][k] = '#'
            elif grid[j][k] == '#' and on != 2 and on != 3:
                nextState[j][k] = '.'
    
    grid = nextState

on  = 0
for j in range(0,len(grid)):
    for k in range(0, len(grid[0])):
        if grid[j][k] == '#':
            on+=1
print(on)



    

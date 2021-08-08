with open(r"input.txt","r") as f:
    tmp = f.read().split("\n")
    grid = []
    for line in tmp:
        tmp2 = []
        for each in line:
            tmp2.append(each)
        grid.append(tmp2)

from copy import deepcopy
from math import atan2

answer = 0

# loop through grid
for y,line in enumerate(grid):
    for x,coord in enumerate(line):
        if coord == '.':
            continue

        counter = set()
        # inner loop searching for asteroids
        for y2 in range(len(grid)):
            for x2 in range(len(grid[0])):
                if y2==y and x2==x:
                    continue
                if grid[y2][x2] == '#':
                    counter.add(atan2(y2-y,x2-x))
        if len(counter) > answer:
            answer = len(counter)
print(answer)
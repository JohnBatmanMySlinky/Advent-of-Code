with open(r"input.txt","r") as f:
    tmp = f.read().split("\n")
    grid = []
    for line in tmp:
        tmp2 = []
        for each in line:
            tmp2.append(each)
        grid.append(tmp2)

from copy import deepcopy
from math import atan2, sqrt, pi
from collections import defaultdict, OrderedDict

answer = [0,0]

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
        if len(counter) > answer[0]:
            answer[0] = len(counter)
            answer[1] = (x,y)
print('part1: {}'.format(answer[0]))



X, Y = answer[1]
# create a sorted list on angle and then by distance
# [[angle, [(distance, coords), (distance, coords)]], [angle, [(distance, coords), (d,c)]]]
# well not only sorted but starts with 90 degrees
# im so bad with coordinates
# this is so clunky
universe_unsorted = defaultdict(list)
test = 0
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if x==X and y==Y:
            pass
        elif grid[y][x] == '#':
            test += 1
            angle = atan2(Y-y,X-x) * 180.0 / pi
            distance = sqrt((y-Y)**2 + (x-X)**2)
            universe_unsorted[angle] += [(distance,x,y)]
        else:
            pass
tmp = []
for k,v in universe_unsorted.items():
    tmp.append([k,sorted(v)])
tmp_sorted = sorted(tmp)

mask_point = [i for i,x in enumerate(tmp_sorted) if x[0]>=90][0]

universe = tmp_sorted[mask_point:len(tmp_sorted)] + tmp_sorted[0:mask_point]

# now I can go thru and pop em out
counter = 0
for x in range(len(universe)):
    potential = universe[x][1]
    if potential:
        counter += 1
        for_print = potential.pop(0)
        if counter == 200:
            print('part2: {}'.format(for_print[1]*100 + for_print[2]))


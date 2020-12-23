import sys
from collections import defaultdict

dat = [x.split('\n') for x in sys.stdin.read().split('\n\n')]

# make input a dictionary
board = defaultdict(list)
for tile in dat:
    for i,x in enumerate(tile):
        if i == 0:
            k = int(x[-5:-1])
        else:
            board[k].append(x)

def rotate(tile):
    newtile = []
    for y in range(len(tile)):
        newrow = ''
        for x in range(len(tile)-1,-1,-1):
            newrow += tile[x][y]
        newtile.append(newrow)
    return(newtile)

def flip_y(tile):
    newtile = []
    for y in range(len(tile)):
        newtile.append(tile[y][::-1])
    return(newtile)

def flip_x(tile):
    newtile = []
    for y in range(len(tile)-1,-1,-1):
        newtile.append(tile[y])
    return(newtile)

# this is resulting in dupes hence set
def all_sides(tile):
    all_sides = set()
    for FX in range(2):
        for FY in range(2):
            for RO in range(4):
                all_sides.add(tile[0])
                tile = rotate(tile)
            tile = flip_y(tile)
        tile = flip_x(tile)
    return(all_sides)
    
# since we only need the corner pieces, 
# they will be the only tiles with two unmatched edges. ha nice
corners = []
for k1,v1 in board.items():
    sides = 0
    for k2,v2 in board.items():
        if len(all_sides(v1) & all_sides(v2))==2:
            sides += 1
    if sides == 2:
        corners.append(k1)

answer = 1
for each in corners:
    answer *= each
print(answer)



        
    
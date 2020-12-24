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

# given a tile
def match_tile(side, tile, dir):
    for FX in range(2):
        for FY in range(2):
            for RO in range(4):
                if side == tile[-1] and dir == "N":
                    return(tile)
                if side == tile[0] and dir == "S":
                    return(tile)
                if side == ''.join([x[-1] for x in tile]) and dir == "W":
                    return(tile)
                if side == ''.join([x[0] for x in tile]) and dir == "E":
                    return(tile)
                tile = rotate(tile)
            tile = flip_y(tile)
        tile = flip_x(tile)
    return([])

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

# TIME TO FIND TOP LEFT
# for c in corners:
for c in [1951]:
    # for each piece that is a corner, loop through all possibilities
    top_left = board[c]
    for FX in range(2):
        for FY in range(2):
            for RO in range(4):

                # now given this rotated corner, find a peice that matches to the south
                for south_id,south in board.items():
                    if c != south_id:
                        south_match = match_tile(top_left[-1], south, "S")
                        if len(south_match) > 1:
                            print(c, south_id)

                            # now given this rotated corner,
                            # and given a match to the south, find an east match (to the corner)
                            for east_id, east in board.items():
                                if c != east_id and south_id != east_id:
                                    east_match = match_tile(''.join([x[-1] for x in top_left]), east, "E")
                                    if len(east_match) > 1:
                                        print(c, south_id, east_id)
                                        assert 5 == 6

                top_left = rotate(top_left)
            top_left = rotate(top_left)
        top_left = rotate(top_left)

# print(flip_x(board[1951]))
# print(flip_x(board[2729]))
# print(match_tile(flip_x(board[1951])[-1],flip_x(board[2729]), "S"))





        
    
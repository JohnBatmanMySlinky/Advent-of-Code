import sys
from collections import defaultdict
import re

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

# given a side of a tile
def match_tile(side, tile, dir):
    for FX in range(2):
        for FY in range(2):
            for RO in range(4):
                if side == tile[0] and dir == "S":
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

answer1 = 1
for c in corners:
    answer1 *= c
print('part1: ' + str(answer1))

# time to find the top left corner
# for c in corners:
def find_top_left(corners):
    for c in corners:
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

                                # now given this rotated corner,
                                # and given a match to the south, find an east match (to the corner)
                                for east_id, east in board.items():
                                    if c != east_id and south_id != east_id:
                                        east_match = match_tile(''.join([x[-1] for x in top_left]), east, "E")
                                        if len(east_match) > 1:
                                            return([c, south_id, east_id], top_left, south_match, east_match)

                    top_left = rotate(top_left)
                top_left = rotate(top_left)
            top_left = rotate(top_left)

# so now we have the top left, south of top left and east of top left
to_be_popped, top_left, south, east = find_top_left(corners)
[board.pop(x) for x in to_be_popped]

# begin building big board, starting with top left
big_board = top_left[:]
big_board += south
for i,x in enumerate(east):
    big_board[i] += x

SIZE = 120

# fill in couth of top left
while len(big_board) < SIZE:
    for south_id, south in board.items():
        south_match = match_tile(big_board[-1], south, "S")
        if len(south_match) > 1:
            break
    board.pop(south_id)
    big_board += south_match

# create big board!
# fill in east, row wise,
# indexing is a little annoying going east
for r in range(int(SIZE/10)):
    while len(big_board[r*10+1]) < SIZE:
        for east_id, east in board.items():
            # getting tiles out of big board
            tile = ''.join([x[-1] for x in big_board[r*10:(r+1)*10]])

            east_match = match_tile(tile, east, "E")
            if len(east_match) > 1:
                break
        board.pop(east_id)
        for i, x in enumerate(east_match):
            big_board[r*10 + i] += x
# now we have a full board :)

# now remove borders
skip_idx = [x+y*10 for x in [0,9] for y in range(int(SIZE/10))]
final_board = []
for x in range(SIZE):
    if x in skip_idx:
        continue
    row = ''
    for y in range(SIZE):
        if y in skip_idx:
            continue
        row += big_board[x][y]
    final_board.append(row)

# now time to find some sea monsters
sea_monster = ['^..................#.$',
               '^#....##....##....###$',
               '^.#..#..#..#..#..#...$']

def find_sea_monster(array):
    one = re.match(sea_monster[0], array[0])
    two = re.match(sea_monster[1], array[1])
    tre = re.match(sea_monster[2], array[2])
    return(one and two and tre)

# why rotate? I don't want to know
final_board = rotate(final_board)

#iterate through rows and lines of final board to find sea monsters
monster_count = 0
for y in range(int(SIZE - 3 - SIZE/10*2)):
    for x in range(int(SIZE - 20 - SIZE/10*2)):

        # build test grid (20,3) for where sea monster would be
        test = []
        for z in range(3):
            test.append(final_board[y+z][x:x+20])

        if find_sea_monster(test):
            monster_count += 1

print('part2: ' + str(sum([x.count('#') for x in final_board])-monster_count*15))



        
    
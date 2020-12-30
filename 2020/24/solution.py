import sys
import re
from collections import deque

dat = [re.findall("e|se|sw|w|nw|ne", x.strip('\n')) for x in sys.stdin]

# wow this is handy
# https://www.redblobgames.com/grids/hexagons/#conversions
move = {
    'e' : [1, -1, 0],
    'se': [0, -1, 1],
    'sw': [-1, 0, 1],
    'w' : [-1, 1, 0],
    'nw': [0, 1, -1],
    'ne': [1, 0, -1]
}

def add(a,b):
    if len(a) == len(b):
        return [a[i] + b[i] for i in range(len(a))]
    else:
        return None

# board holds all tiles that have been flipped
board = []
for dir in dat:
    # figure out which tile gets flipped
    tile = [0, 0, 0]
    for step in dir:
        tile = add(tile, move[step])

    # if tile in board, remove it. else add it.
    if tile in board:
        board.remove(tile)
    else:
        board.append(tile)
print('part1: ' + str(len(board)))

# PART 2
# white with 2 adj --> black
def day(oldblack):
    white = deque()
    white_x = [x[0] for x in oldblack]
    white_y = [x[1] for x in oldblack]
    white_z = [x[2] for x in oldblack]
    for x in range(min(white_x)-1,max(white_x)+2):
        for y in range(min(white_y)-1,max(white_y)+2):
            for z in range(min(white_z)-1,max(white_z)+2):
                if x+y+z == 0:
                    white.append([x,y,z])

    newblack = deque()
    for B in oldblack:
        black_adjacent = 0
        for adj in list(move.keys()):
            neighbor = add(B, move[adj])
            if neighbor in oldblack:
                black_adjacent += 1
        if black_adjacent == 1 or black_adjacent == 2:
            if B not in newblack:
                newblack.append(B)
                
    for W in white:
        black_adjacent = 0
        for adj in list(move.keys()):
            neighbor = add(W, move[adj])
            if neighbor in oldblack:
                black_adjacent += 1
        if black_adjacent == 2:
            if W not in newblack:
                newblack.append(W)

    return(list(newblack))


for john in range(100):
    if john % 10 == 0:
        print(john)
    board = day(board)
print(len(board))
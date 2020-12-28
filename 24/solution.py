import sys
import re

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
print(len(board))


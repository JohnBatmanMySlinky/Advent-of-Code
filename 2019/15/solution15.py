with open(r"input.txt","r") as f:
    raw = [x.split(",") for x in f.readlines()][0]
    orig = [int(x) for x in raw]
    orig += [0 for x in range(1_000_000)]

import operator
import random
from collections import defaultdict

def return_params(raw, pos, mode, rb):
    # position
    if mode == 0:
        return raw[raw[pos]]
    # immediate
    elif mode == 1:
        return raw[pos]
    # offset
    elif mode == 2:
        return raw[raw[pos]+rb]
    else:
        return None

math = {
    1: operator.add,
    2: operator.mul,
    5: operator.ne,
    6: operator.eq,
    7: operator.lt,
    8: operator.eq
}


def INTCODE(orig, INPUT, pos, rb):
    raw = orig.copy()
    while True:
        op = str(raw[pos]).rjust(5,'0')
        A, B, C, DE = int(op[0]), int(op[1]), int(op[2]), int(op[3:5])

        if DE == 1 or DE == 2:
            x = return_params(raw, pos+1, C, rb)
            y = return_params(raw, pos+2, B, rb)

            if A == 2:
                rb_maybe = rb
            else:
                rb_maybe = 0
            raw[raw[pos + 3]+rb_maybe] = math[DE](x,y)

            pos += 4
        elif DE == 3:
            x = INPUT.pop(0)
            if C == 2:
                raw[raw[pos + 1]+rb] = x
            else:
                raw[raw[pos + 1]] = x
            pos += 2
        elif DE == 4:
            x = return_params(raw, pos+1, C, rb)
            pos += 2
            return raw, x, pos, rb, 0
        elif DE == 5 or DE == 6:
            x = return_params(raw, pos+1, C, rb)
            if math[DE](x, 0):
                pos = return_params(raw, pos+2, B, rb)
            else:
                pos += 3
        elif DE == 7 or DE == 8:
            x = return_params(raw, pos+1, C, rb)
            y = return_params(raw, pos+2, B, rb)
            if A == 2:
                rb_maybe = rb
            else:
                rb_maybe = 0
            if math[DE](x,y):
                raw[raw[pos+3]+rb_maybe] = 1
            else:
                raw[raw[pos+3]+rb_maybe] = 0
            pos += 4
        elif DE == 9:
            rb += return_params(raw, pos+1, C, rb)
            pos += 2
        elif DE == 99:
            print('99')
            return None, None, None, None, 99

def update_pos(pos, b):
    if b == 1:
        pos[0] -= 1 # north moves one vertical, one less index
    elif b == 2:
        pos[0] += 1 # south moves one vertical, one more index
    elif b == 3:
        pos[1] += 1 # east is + 1
    elif b == 4:
        pos[1] -= 1 # west is -1

    return pos

def update_board(board, pos, b, b_out):
    if b == 1:
        board[pos[0] - 1][pos[1]] = b_out
    elif b == 2:
        board[pos[0] + 1][pos[1]] = b_out
    elif b == 3:
        board[pos[0]][pos[1] + 1] = b_out
    elif b == 4:
        board[pos[0]][pos[1] - 1] = b_out

    return board

def generate_next(pos, move):
    if move == 1:
        out = (pos[0] + 1, pos[1])
    elif move == 2:
        out = (pos[0] - 1, pos[1])
    elif move == 3:
        out = (pos[0], pos[1] + 1)
    elif move == 4:    
        out = (pos[0], pos[1] - 1)
    return out


a = orig.copy()
b = 1
c, d, e = 0, 0, 0
pos = (0,0)
queue = [(pos, a, c, d)]
path = set()
path.add(pos)

# find oxygen
while queue:
    pos, a, c, d = queue.pop(0)    
    for move in [1,2,3,4]:
        board, tile, c_out, d_out, e = INTCODE(a, [move], c, d)
        if tile == 0:
            pass
        elif tile == 1:
            if generate_next(pos, move) not in path:
                queue.append((
                    generate_next(pos, move),
                    board, c, d
                ))
                path.add(generate_next(pos,move))
        elif tile == 2:
            oxygen = pos
            print('yeehaw found oxygen at {}'.format(oxygen))
        else: 
            break

print('finished filling in full grid. explored {} tiles'.format(len(path)))


# part 1 BFS
# figure out how far away it is
pos = (0,0)
visited = []
queue = []

def BFS(visited, queue, graph, node, end):
    visited.append(node)
    queue.append((node,1))

    while queue:
        s, d = queue.pop(0)
        if s == end:
            return d
        for neighbour in [generate_next(s,y) for y in range(1,5)]:
            if neighbour in path:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append((neighbour, d+1))

# finish part 1
part1 = BFS(visited, queue, path, oxygen, pos)
print("part1: {}".format(part1))



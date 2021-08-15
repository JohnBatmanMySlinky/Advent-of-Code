with open(r"input.txt","r") as f:
    raw = [x.split(",") for x in f.readlines()][0]
    orig = [int(x) for x in raw]
    orig += [0 for x in range(1_000_000)]

import operator
import pdb

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


# 0 in if black
# 1 in if white

# 0 --> print black
# 1 --> print white
# =================
# 0 --> turn left
# 1 --> turn right

def turn_and_move(coords, direction, turn):
    # 0 --> up
    # 1 --> right
    # 2 --> down
    # 3 --> left
    if turn == 0:
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4

    if direction == 0:  # up
        pos = (coords[0], coords[1] + 1)
    elif direction == 1:  # right
        pos = (coords[0] + 1, coords[1])
    elif direction == 2:  # down
        pos = (coords[0], coords[1] - 1)
    elif direction == 3:  # left
        pos = (coords[0] - 1, coords[1])

    return pos, direction


########### PART 1
board = {(0,0):0}
direction = 0
coords = (0,0)
a = orig.copy()
input = 0
c = 0
d = 0
e = 0
print("this works, just takes a while...")
while e != 99:
    a, b, c, d, e = INTCODE(a, [input], c, d)
    if e == 99: break
    paint = b
    a, b, c, d, e = INTCODE(a, [input], c, d)
    turn = b

    board[coords] = paint

    coords, direction = turn_and_move(coords, direction, turn)
    if coords in board.keys():
        input = board[coords]
    else:
        input = 0
print("part1: {}".format(len(board.keys())))


########### PART 2
# it do be sideways
board = {(0,0):1}
direction = 0
coords = (0,0)
a = orig.copy()
input = 1
c = 0
d = 0
e = 0
while e != 99:
    a, b, c, d, e = INTCODE(a, [input], c, d)
    if e == 99: break
    paint = b
    a, b, c, d, e = INTCODE(a, [input], c, d)
    turn = b

    board[coords] = paint

    coords, direction = turn_and_move(coords, direction, turn)
    if coords in board.keys():
        input = board[coords]
    else:
        input = 0

painting = [[' ']*20 for x in range(50)]
for k, v in board.items():
    if v == 1:
        painting[k[0]+10][k[1]+10] = '#'
print(painting)


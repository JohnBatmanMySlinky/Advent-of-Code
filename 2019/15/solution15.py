with open(r"input.txt","r") as f:
    raw = [x.split(",") for x in f.readlines()][0]
    orig = [int(x) for x in raw]
    orig += [0 for x in range(1_000_000)]

import operator
import random

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


a = orig.copy()
b = 1
c, d, e = 0, 0, 0
N = 45
board = [[8 for x in range(N)] for y in range(N)]
pos = [N//2, N//2]
board[pos[0]][pos[1]] = 1
i = 1

while e != 99:
    a, b_out, c, d, e = INTCODE(a, [b], c, d)

    board = update_board(board, pos, b, b_out)

    if b_out == 2:
        print('YEEEEEHAW')
        print(board)
        break

    if b_out != 0:
        pos = update_pos(pos, b)

    # print("current position: ({}, {})".format(pos[0], pos[1]))
    # print("direction input:   {}".format(b))
    # print("output tile:       {}".format(b_out))
    # print("iteration:         {:,}".format(i))
    if i % 1000 == 0:
        print(i)
        print(board)
        print("==============================================================")
    # b = int(input())
    if b_out == 0:
        b = random.sample([x for x in range(1,5) if x is not b], 1)[0]
    else:
        b = random.sample([1,2,3,4],1)[0]
    i += 1
with open(r"input.txt","r") as f:
    raw = [x.split(",") for x in f.readlines()][0]
    orig = [int(x) for x in raw]

import operator as operator
from itertools import permutations

def return_params(raw, pos, mode):
    if mode == 0:
        return raw[raw[pos]]
    elif mode == 1:
        return raw[pos]
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

def INTCODE(orig, INPUT, pos):
    raw = orig.copy()
    while True:
        op = str(raw[pos]).rjust(5,'0')
        A, B, C, DE = int(op[0]), int(op[1]), int(op[2]), int(op[3:5])

        if DE == 1 or DE == 2:
            x = return_params(raw, pos+1, C)
            y = return_params(raw, pos+2, B)

            raw[raw[pos + 3]] = math[DE](x,y)

            pos += 4
        elif DE == 3:
            x = INPUT.pop(0)
            raw[raw[pos + 1]] = x
            pos += 2
        elif DE == 4:
            x = return_params(raw, pos+1, C)
            pos += 2
            return raw, x, pos, 0
        elif DE == 5 or DE == 6:
            x = return_params(raw, pos+1, C)
            if math[DE](x, 0):
                pos = return_params(raw, pos+2, B)
            else:
                pos += 3
        elif DE == 7 or DE == 8:
            x = return_params(raw, pos+1, C)
            y = return_params(raw, pos+2, B)
            if math[DE](x,y):
                raw[raw[pos+3]] = 1
            else:
                raw[raw[pos+3]] = 0
            pos += 4
        elif DE == 99:
            return None, None, None, 99

universe = permutations(range(5,10))
winner = 0
for u in universe:
    # init
    a1, a2, a3, win = INTCODE(orig, [u[0],0], 0)
    b1, b2, b3, win = INTCODE(orig, [u[1],a2], 0)
    c1, c2, c3, win = INTCODE(orig, [u[2],b2], 0)
    d1, d2, d3, win = INTCODE(orig, [u[3],c2], 0)
    e1, e2, e3, win = INTCODE(orig, [u[4],d2], 0)

    while e2:
        log = e2
        a1, a2, a3, win = INTCODE(a1, [e2], a3)
        b1, b2, b3, win = INTCODE(b1, [a2], b3)
        c1, c2, c3, win = INTCODE(c1, [b2], c3)
        d1, d2, d3, win = INTCODE(d1, [c2], d3)
        e1, e2, e3, win = INTCODE(e1, [d2], e3)
    if log > winner:
        winner = log
print(winner)




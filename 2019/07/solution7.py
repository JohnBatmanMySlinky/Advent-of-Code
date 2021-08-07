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

def INTCODE(orig, INPUT, part):
    raw = orig.copy()
    pos = 0
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
            return x
            pos += 2
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
            break

universe = permutations(range(5))
winner = [0,(0,0,0,0,0)]
for u in universe:
    test = [[u[0],0], [u[1],None], [u[2], None], [u[3], None], [u[4], None]]
    for idx in range(5):
        if idx < 4:
            test[idx+1][1] = INTCODE(orig, test[idx], 'one')
        else:
            score = INTCODE(orig, test[idx], 'one')
    if score > winner[0]:
        winner[0] = score
        winner[1] = u
print('part1: {}'.format(winner[0]))


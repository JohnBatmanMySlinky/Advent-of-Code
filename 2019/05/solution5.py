with open(r"input.txt","r") as f:
    raw = [x.split(",") for x in f.readlines()][0]
    orig = [int(x) for x in raw]

import operator as operator


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
            raw[raw[pos + 1]] = INPUT
            pos += 2
        elif DE == 4:
            x = return_params(raw, pos+1, C)
            print(x)
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
    return('^^part {}^^'.format(part))


print(INTCODE(orig, 1, 'one'))
print(INTCODE(orig, 5, 'two'))
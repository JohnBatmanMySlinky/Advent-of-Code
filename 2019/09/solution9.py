with open(r"input.txt","r") as f:
    raw = [x.split(",") for x in f.readlines()][0]
    orig = [int(x) for x in raw]
    orig += [0 for x in range(1_000_000)]

# orig = [109, -1, 4, 1, 99] # - 1
# orig = [109, -1, 104, 1, 99] # 1
# orig = [109, -1, 204, 1, 99] # 109
# orig = [109, 1, 9, 2, 204, -6, 99] # 204
# orig = [109, 1, 109, 9, 204, -6, 99] # 204
# orig = [109, 1, 209, -1, 204, -106, 99] # 204
# orig = [109, 1, 3, 3, 204, 2, 99] # input
# orig = [109, 1, 203, 2, 204, 2, 99] # input
# orig = [109, 1, 203, 2, 2201, 1, 1, 3, 204, 2, 99] # input

import operator

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


def INTCODE(orig, INPUT, pos):
    raw = orig.copy()
    rb = 0
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
            return raw, x, pos, 0
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
            return None, None, None, 99


print(INTCODE(orig, [1], 0)[1])
with open(r"input.txt","r") as f:
    raw = [x.split(",") for x in f.readlines()][0]
    raw = [int(x) for x in raw]



def return_params(raw, pos, mode):
    if mode == 0:
        return raw[raw[pos]]
    elif mode == 1:
        return raw[pos]
    else:
        return None

#part 1
pos = 0
while True:
    op = str(raw[pos]).rjust(5,'0')
    A, B, C, DE = int(op[0]), int(op[1]), int(op[2]), int(op[3:5])

    if DE == 1 or DE == 2:
        x = return_params(raw, pos+1, C)
        y = return_params(raw, pos+2, B)
        if DE == 1:
            raw[raw[pos + 3]] = x + y
        elif DE == 2:
            raw[raw[pos + 3]] = x * y
        pos += 4
    elif DE == 3:
        print('input code pls')
        raw[raw[pos + 1]] = int(input())
        pos += 2
    elif DE == 4:
        x = return_params(raw, pos+1, C)
        if x != 0:
            print(f'part1: {x}')
        else:
            print(x)
        pos += 2
    elif DE == 99:
        break

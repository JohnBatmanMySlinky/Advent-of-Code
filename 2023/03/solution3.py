def p1():
    with open("input.txt", "r") as f:
        board = [x.strip() for x in f.readlines()]
    numbers = find_number_idx(board)
    score = 0

    for number, idxs in numbers:
        has_neighbors = [has_neighbor(board, idx) for idx in idxs]
        if any(has_neighbors):
            score += number
    return score

def p2():
    with open("input.txt", "r") as f:
        board = [x.strip() for x in f.readlines()]
    numbers = find_number_idx(board)
    symbols = find_symbols(board)

    gearratios = 0
    for gear in symbols:
        gearratios += gear_math(board, numbers, gear)

    return gearratios


def gear_math(board, numbers, gear):
    Y = len(board)
    X = len(board[0])
    x,y = gear
    tmpscore = set()
    for xo in [-1,0,1]:
        for yo in [-1,0,1]:
            if (y+yo < 0) | (y+yo==Y) | (x+xo < 0) | (x+xo==X):
                continue
            # print(f"({x},{y}): {x+xo},{y+yo}")
            newidx = (x+xo, y+yo)
            for number, numidxs in numbers:
                if newidx in numidxs:
                    tmpscore.add(number)
                    # print(f"hit: {tmpscore}")
                if len(tmpscore)==2:
                    asdf = list(tmpscore)
                    return asdf[0] * asdf[1]
    return 0

def find_symbols(board):
    symbols = []
    Y = len(board)
    X = len(board[0])

    for y in range(Y):
        for x in range(X):
            if board[y][x] == "*":
                symbols.append((x,y))
    return symbols

def has_neighbor(board, idx):
    Y = len(board)
    X = len(board[0])
    x,y = idx

    for yo in [1,0,-1]:
        for xo in [1,0, -1]:
            if (y+yo < 0) | (y+yo==Y) | (x+xo < 0) | (x+xo==X):
                continue
            tmp = board[y+yo][x+xo]
            if not (tmp.isdigit() | (tmp == ".")):
                return True
    return False

     

def find_number_idx(board):
    numbers = []
    Y = len(board)
    X = len(board[0])

    for y in range(Y):
        tmpidx = []
        tmpnum = ""
        for x in range(X):
            current = board[y][x]
            if current.isdigit():
                tmpidx.append((x,y))
                tmpnum += current
            else: # reset on non-digit
                if len(tmpidx) > 0:
                    numbers.append([int(tmpnum), tmpidx])
                    tmpidx = []
                    tmpnum = ""
        if tmpidx: # reset at end of row
            numbers.append([int(tmpnum), tmpidx])
            tmpidx = []
            tmpnum = ""
    return numbers

a1 = p1()
print(f"Part 1: {a1}")
a2 = p2()
print(f"Part 2: {a2}")
import copy

def parse():
    with open("input.txt", "r") as f:
        raw = [list(x.strip()) for x in f.readlines()]
    return raw

def findS(board):
    Y = len(board)
    X = len(board[0])
    for x in range(X):
        for y in range(Y):
            if board[y][x] == "S":
                return x,y
            
def findmax(board):
    Y = len(board)
    X = len(board[0])
    maxx = 0
    for x in range(X):
        for y in range(Y):
            if board[y][x] not in ["S", "F", "J", "7", "L", "-", "|", "."]:
                if board[y][x] > maxx:
                    maxx = board[y][x]
    return maxx

def traverse(board):
    Y = len(board)
    X = len(board[0])

    distance = copy.deepcopy(board)

    x, y = findS(board)
    board[y][x] = "|"
    distance[y][x] = 0
    que = [(x,y)]
    moves = [(1,0), (-1,0), (0,1), (0,-1)]
    seen = set()
    # X, Y notation
    valid = {
        ( 1,  0): ("-", "J", "7"),
        (-1,  0): ("-", "F", "L"),
        ( 0, -1): ("|", "F", "7"),
        ( 0,  1): ("|", "L", "J"),
    }
    valid = {
        "-": [
            ((-1, 0), "-"),
            ((-1, 0), "L"),
            ((-1, 0), "F"),
            (( 1, 0), "-"),
            (( 1, 0), "J"),
            (( 1, 0), "7"),
        ],
        "|": [
            ((0,  1), "|"),
            ((0,  1), "J"),
            ((0,  1), "L"),
            ((0, -1), "|"),
            ((0, -1), "F"),
            ((0, -1), "7"),
        ],
        "J": [
            ((-1,  0), "-"),
            ((-1,  0), "L"),
            ((-1,  0), "F"),
            (( 0, -1), "|"),
            (( 0, -1), "F"),
            (( 0, -1), "7"),
        ],
        "7": [
            ((-1, 0), "-"),
            ((-1, 0), "L"),
            ((-1, 0), "F"),
            (( 0, 1), "|"),
            (( 0, 1), "L"),
            (( 0, 1), "J"),
        ],
        "L": [
            ((0, -1), "|"),
            ((0, -1), "7"),
            ((0, -1), "F"),
            ((1,  0), "-"),
            ((1,  0), "J"),
            ((1,  0), "7"),
        ],
        "F": [
            ((0, 1), "|"),
            ((0, 1), "L"),
            ((0, 1), "J"),
            ((1, 0), "-"),
            ((1, 0), "7"),
            ((1, 0), "J"),
        ]
    }

    while que:
        x,y = que.pop(0)
        for move in moves:
            xo, yo = move
            if (x+xo, y+yo) not in seen:
                if (y + yo >= 0) & (y + yo < Y) & (x + xo >= 0) & (x + xo < X):
                    curr = board[y][x]
                    new = board[y+yo][x+xo]
                    if ((xo,yo), new) in valid[curr]:
                        distance[y+yo][x+xo] = distance[y][x] + 1
                        que.append((x+xo, y+yo))
                        seen.add((x+xo, y+yo))
                        # print(distance)
                        # input()
    winner = findmax(distance)
    return winner, distance

def p1():
    data = parse()
    maxdistance, _ = traverse(data)
    return maxdistance


def is_inside(board, cell):
    X = len(board[0])
    x,y = cell
    bar_count = 0
    c_up = 0
    c_down = 0
    for xo in range(1,X-x):
        if board[y][x+xo] == "|":
            bar_count += 1
        if board[y][x+xo] in ["L", "J"]:
            c_up += 1
        if board[y][x+xo] in ["F", "7"]:
            c_down += 1

    if bar_count > 0:
        if bar_count % 2 == 0:
            return False
        else:
            return True
    elif (c_up > 0) | (c_down > 0):
        if (c_up % 2 == 0) & (c_down % 2 == 0):
            return False
        else:
            return True
    else:
        return True


def floodfill(board):
    Y = len(board)
    X = len(board[0])

    # get set of tiles that  are NOT pipe tiles
    non_pipes = []
    for x in range(X):
        for y in range(Y):
            if board[y][x] == ".":
                non_pipes.append((x,y))

    # Fill all floods
    floods = []
    seen = set()
    while non_pipes:
        curr = non_pipes.pop(0)
        if curr in seen:
            continue
        seen.add(curr)
        que = [curr]
        flood = [curr]
        while que:
            x,y = que.pop(0)
            seen.add((x,y))
            for xo, yo in [(1,0), (-1,0), (0,1), (0,-1)]:
                xx = x+xo
                yy = y+yo
                if (xx < 0) | (xx == X) | (yy < 0) | (yy == Y):
                    continue
                elif (board[yy][xx] != "."):
                    continue
                elif ((xx,yy) in seen): 
                    continue
                elif board[yy][xx] == ".":
                    que.append((xx, yy))
                    flood.append((xx, yy))
                    seen.add((xx, yy))
                else:
                    assert False
        floods.append(flood)

    # now all floods are built, prune the edge cases
    prunedfloods = []
    for flood in floods:
        kill = False
        for x,y in flood:
            if (x == 0) | (x == X-1) | (y == 0) | (y == Y-1):
                kill = True
        if not kill:
            prunedfloods.append(flood)
    return prunedfloods

def p2():
    data = parse()
    # this mutates data
    _, pipes = traverse(data)

    # use pipes to mask non-pipe pieces
    data = parse()
    X = len(data[0])
    Y = len(data)
    for x in range(X):
        for y in range(Y):
            if not str(pipes[y][x]).isdigit():
                data[y][x] = "."
    # print(pipes)
    # print(data)

    floods = floodfill(pipes)
    score = 0
    for flood in floods:
        if is_inside(data, flood[0]):
            score += len(flood)
    return score




a1 = p1()
print(f"Part 1: {a1}")
a2 = p2()
print(f"Part 2: {a2}")
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

    while que:
        x,y = que.pop(0)
        for move in moves:
            xo, yo = move
            if (x+xo, y+yo) not in seen:
                if (y + yo >= 0) & (y + yo < Y) & (x + xo >= 0) & (x + xo < X):
                    new = board[y+yo][x+xo]
                    if new in valid[(xo, yo)]:
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

def floodfill(board):
    Y = len(board)
    X = len(board[0])

    # get set of tiles that  are NOT pipe tiles
    non_pipes = set()
    for x in range(X):
        for y in range(Y):
            if board[y][x] == ".":
                non_pipes.add((x,y))

    # the fill
    floods = []
    seen = set()
    while non_pipes:
        # pick a non-pipe to start with and flood fill. 
        curr = non_pipes.pop()
        seen.add(curr)
        que = [curr]
        flood = [curr]
        poisonpill = True
        while que:
            x,y = que.pop(0)
            for xo, yo in [(1,0), (-1,0), (0,1), (0,-1)]:
                xx = x+xo
                yy = y+yo
                # print(f"\t: working with {xx}, {yy}")
                if (xx < 0) | (xx == X) | (yy < 0) | (yy == Y):
                    # out of bounds. Stop filling.
                    que = []
                    poisonpill = True
                    break
                elif (board[yy][xx] != "."):
                    #if we hit a pipe, do nothing
                    pass
                elif ((xx,yy) in seen): 
                    # if we visit a seen, do nothing
                    pass
                elif board[yy][xx] == ".":
                    poisonpill = False
                    que.append((xx, yy))
                    flood.append((xx,yy))
                    seen.add((xx,yy))
                else:
                    # i think 
                    assert False
        if not poisonpill:
            floods.append(flood)
    return floods

def p2():
    data = parse()
    _, pipes = traverse(data)
    floods = floodfill(pipes)
    score = 0
    for flood in floods:
        score += len(flood)
    return score




a1 = p1()
print(f"Part 1: {a1}")
a2 = p2()
print(f"Part 2: {a2}")
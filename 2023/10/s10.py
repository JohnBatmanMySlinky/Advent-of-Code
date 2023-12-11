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
    print(distance)
    winner = findmax(distance)
    return winner

def p1():
    data = parse()
    newboard = traverse(data)
    return newboard

a1 = p1()
print(f"Part 1: {a1}")
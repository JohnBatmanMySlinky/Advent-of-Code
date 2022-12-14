with open("input.txt") as f:
    data = [[list(map(int,y.split(","))) for y in x.strip().split(' -> ')] for x in f.readlines()]

def draw_board(data):
    # get board
    xx = []
    yy = []
    for wall in data:
        for x,y in wall:
            xx.append(x)
            yy.append(y)
    maxx = max(xx)
    minx = min(xx)-5
    maxy = max(yy)
    miny = 0
    spanx = maxx - minx
    spany = maxy - miny
    board = [['.' for _ in range(spanx+10)] for _ in range(spany+3)]
    #print(f"max x: {maxx}, max y: {maxy}, min x: {minx}, min y: {miny}, span x: {spanx}, span y: {spany}")

    # draw board
    for wall in data:
        finish = wall.pop(0)
        for segment in wall:
            start = segment[:]
            for x in range(min(start[0],finish[0])-minx,max(start[0],finish[0])-minx+1):
                for y in range(min(start[1],finish[1])-miny,max(start[1],finish[1])-miny+1):
                    board[y][x] = "#"
            finish = start[:]

    return board, maxy, minx


def can_move(board, x, y):
    for dx,dy in [[0,1], [-1,1], [1,1]]:
        if board[y+dy][x+dx] == ".":
            return dx, dy
    return None

def p1(data, N):
    winner = 0
    board, floor, offset = draw_board(data)
    for o in range(N):
        winner += 1
        posx = 500
        posy = 0
        if board[posy][posx-offset] == 'o':
            return winner
        else:
            while True:
                nextmove = can_move(board, posx-offset, posy)
                if nextmove:
                    dx, dy = nextmove
                    board[posy][posx-offset] = '.'
                    board[posy+dy][posx+dx-offset] = 'o'
                    posy += dy
                    posx += dx
                    if posy == floor:
                        return winner-1
                    #print(board)
                    #input()
                else:
                    break
    return None

print(f"{p1(data, 1000)}")
with open('input.txt') as f:
    raw = [x.strip().split(',') for x in f.readlines()]
    coords = []
    folds = []
    for each in raw:
        if len(each)==1:
            if each[0].find('fold')>-1:
                tmp = each[0].split('=')
                folds.append([tmp[0][-1], int(tmp[1])])
        else:
            coords.append([int(each[0]),int(each[1])])  


def fold(board, a, b):
    if a == 'y':
        new = []
        old = []
        for x in range(len(board)):
            if x < b:
                new.append(board[x])
            elif x>b:
                old.append(board[x])
        
        offset = len(new)-1
        for y in range(len(new)):
            for x in range(len(new[0])):
                new[y][x] = max(new[y][x],old[offset-y][x])
    if a == 'x':
        new = []
        old = []
        for x in range(len(board)):
            new.append(board[x][:b])
            old.append(board[x][(b+1):])

        offset = len(new[0])-1
        for y in range(len(new)):
            for x in range(len(new[0])):
                new[y][x] = max(new[y][x], old[y][offset-x])

    return new


def solve(coords, folds, part):
    maxx = max([x for x,y in coords])
    maxy = max([y for x,y in coords])
    board = [[0 for x in range(2000+1)] for y in range(2000+1)]
    for x,y in coords:
        board[y][x] = 1


    for a,b in folds:
        board = fold(board, a, b)
        if part == 1:
            return sum([sum(x) for x in board])
    
    pretty = []
    for y in range(len(board)):
        row = ''
        for x in range(len(board[0])):
            if board[y][x] == 1:
                row += '#'
            else:
                row += ' '
        pretty.append(row)

    return pretty

        


print(solve(coords, folds, 1))
print(solve(coords, folds, 2))
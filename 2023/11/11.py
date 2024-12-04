from copy import deepcopy

def transpose(l1):
    l2 = []
    for i in range(len(l1[0])):
        row = []
        for item in l1:
            row.append(item[i])
        l2.append(row)
    return l2

def expand(board):
    new_board = deepcopy(board)
    offset = 0
    for i,row in enumerate(board):
        if all([x=="." for x in row]):
            new_board.insert(i+1+offset,row)
            offset += 1
    return new_board


def fake_expand(board):
    expanded = []
    for i, row in enumerate(board):
        if all([x=="." for x in row]):
            expanded += [i]
    return expanded


def part1():
    with open("input.txt", "r") as f:
        board = [list(x.strip()) for x in f.readlines()]

    board = expand(board)
    board = transpose(board)
    board = expand(board)
    board = transpose(board)

    galaxies = set()

    for x in range(len(board[0])):
        for y in range(len(board)):
            if board[y][x] == "#":
                galaxies.add((x,y))

    answer = 0
    for g1 in galaxies:
        for g2 in galaxies:
            answer += abs(g1[0]-g2[0]) + abs(g1[1]-g2[1])
    return int(answer/2)

def part2(N):
    with open("input.txt", "r") as f:
        board = [list(x.strip()) for x in f.readlines()]

    ROWS = fake_expand(board)
    board = transpose(board)
    COLS = fake_expand(board)
    board = transpose(board)

    galaxies = set()

    for x in range(len(board[0])):
        for y in range(len(board)):
            if board[y][x] == "#":
                galaxies.add((x,y))

    answer = 0
    for g1 in galaxies:
        for g2 in galaxies:
            x1 = min(g1[0], g2[0])
            x2 = max(g1[0], g2[0])
            y1 = min(g1[1], g2[1])
            y2 = max(g1[1], g2[1])

            row_mult = 0
            for x in COLS:
                if (x1 < x < x2) or (x2 < x < x1):
                    row_mult += 1
            col_mult = 0
            for y in ROWS:
                if (y1 < y < y2) or (y2 < y < y1):
                    col_mult += 1
            answer += abs(g1[0]-g2[0]) + abs(g1[1]-g2[1]) + (N-1)*row_mult + (N-1)*col_mult
    return int(answer/2)

print(f"part 1: {part1()}")
print(f"part 2: {part2(1_000_000)}")






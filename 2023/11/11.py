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

print(f"part 1: {part1()}")






def valid(board, current, offset):
    x = current[0] + offset[0]
    y = current[1] + offset[1]
    if x < 0 or x >= len(board[0]) or y < 0 or y >= len(board):
        return False
    return True

def found_already(new, found):
    for each in found:
        if set(each) == set(new):
            return True
    return False

def part1():
    with open("input.txt", "r") as f:
        board = [x.strip() for x in f.readlines()]

    moves = [
        [(0,0), (0,1), (0,2), (0,3)], # plus y
        [(0,0), (0,-1), (0,-2), (0,-3)], # minus y
        [(0,0), (1,0), (2,0), (3,0)], # plus x
        [(0,0), (-1,0), (-2,0), (-3,0)], # minus x
        [(0,0), (1,1), (2,2), (3,3)], # down right
        [(0,0), (-1,-1), (-2,-2), (-3,-3)], # up left
        [(0,0), (1,-1), (2,-2), (3,-3)],
        [(0,0), (-1,1), (-2,2), (-3,3)],
    ]

    answers = ("XMAS", "SAMX")

    winners = 0
    found = set()
    for x in range(len(board[0])):
        for y in range(len(board)):
            for move in moves:
                collected = ""
                pos = []
                for xo, yo in move:
                    if valid(board, (x,y), (xo,yo)):
                        collected += board[y+yo][x+xo]
                        pos += [(x+xo,y+yo)]
                    else:
                        break
                if (collected in answers) and not(found_already(tuple(pos), found)):
                    winners += 1
                    found.add(tuple(pos))
    return winners


def part2():
    with open("input.txt", "r") as f:
        board = [x.strip() for x in f.readlines()]

    moves = [
        [
            (-1,-1),        (1,-1),
                     (0,0),
            (-1,1),         (1,1),
        ]
    ]

    answers = ("MSAMS", "MMASS", "SMASM", "SSAMM")

    winners = 0
    found = set()
    for x in range(len(board[0])):
        for y in range(len(board)):
            for move in moves:
                collected = ""
                pos = []
                for xo, yo in move:
                    if valid(board, (x,y), (xo,yo)):
                        collected += board[y+yo][x+xo]
                        pos += [(x+xo,y+yo)]
                    else:
                        break
                if (collected in answers):
                    winners += 1
                    found.add(tuple(pos))
    return winners



print(f"part 1: {part1()}")
print(f"part 2: {part2()}")





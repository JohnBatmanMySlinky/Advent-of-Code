def move(board, mapper, current, dir, seen):
    x,y = current
    xo, yo = mapper[dir]
    for i in range(1,len(board)-1):
        if (x+xo*i<0) or (x+xo*i==len(board)) or (y+yo*i<0) or (y+yo*i==len(board)):
            break
        elif board[y+yo*i][x+xo*i] == ".":
            seen.add((x+xo*i,y+yo*i))
        elif board[y+yo*i][x+xo*i] == "#":
            return (True, (x+xo*(i-1), y+yo*(i-1)), seen)
    return False, (-9999999, -9999999), seen
        


def part1():
    with open("input.txt", "r") as f:
        board = [list(x.strip()) for x in f.readlines()]

    assert len(board) == len(board[0])

    mapper = {
        "^": (0, -1),
        ">": (1, 0),
        "V": (0, 1),
        "<": (-1, 0),
    }

    for x in range(len(board)):
        for y in range(len(board)):
            if board[y][x] in mapper.keys():
                pos = (x,y)
                dir = board[y][x]
    OK = True
    seen = set()
    seen.add(pos)
    move_idx = 0
    while OK:
        OK, pos, seen = move(board, mapper, pos, dir, seen)
        if OK:
            move_idx += 1
            move_idx %= 4
            dir = list(mapper.keys())[move_idx]

    return len(seen)

print(f"part 1: {part1()}")
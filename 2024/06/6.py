from copy import deepcopy

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

def move_inf(board, mapper, current, dir):
    xx,yy = current
    xo, yo = mapper[dir]
    segment = set()
    i = 0
    while True:
        if (xx+xo*i<0) or (xx+xo*i==len(board)) or (yy+yo*i<0) or (yy+yo*i==len(board)):
            break
        elif board[yy+yo*i][xx+xo*i] == ".":
            segment.add((xx+xo*i,yy+yo*i))
        elif board[yy+yo*i][xx+xo*i] == "#":
            return (True, (xx+xo*(i-1), yy+yo*(i-1)), segment)
        
        i += 1
    return False, (-9999999, -9999999), segment
        


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


def part2():
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
                origin = (x,y)
                origin_dir = board[y][x]
    
    answer = 0
    N = len(board)
    for x in range(len(board)):
        for y in range(len(board)):        
            new_board = deepcopy(board)
            if new_board[y][x] == "#" or (x,y) == origin:
                pass
            elif (board[y][x] == "."):
                new_board[y][x] = "#"

            OK = True
            segments = []
            n_segments = 0
            move_idx = 0
            pos = origin
            dir = origin_dir
            while OK:
                OK, pos, segment = move_inf(new_board, mapper, pos, dir)
                if segment in segments:
                    n_segments += 1
                else:
                    segments += [segment]

                if n_segments > 15:
                    answer += 1
                    OK = False

                if OK:
                    move_idx += 1
                    move_idx %= 4
                    dir = list(mapper.keys())[move_idx]
    return answer


print(f"part 1: {part1()}")
print(f"part 2: {part2()}")
def make_grid(serial, SIZE):
    grid = [[0 for x in range(SIZE)] for y in range(SIZE)]

    for x in range(SIZE):
        for y in range(SIZE):
            rack_id = x+1 + 10
            grid[x][y] = int(str(((rack_id * (y+1)) + serial) * rack_id)[-3:-2]) - 5

    return grid


def p1(grid):
    winner = -100
    winner_coord = (-1, -1)
    offsets = [(x,y) for x in [-1, 0, 1] for y in [-1, 0, 1]]
    for x in range(1,len(grid)-1):
        for y in range(1,len(grid)-1):
            tot = 0
            for xo, yo in offsets:
                tot += grid[x+xo][y+yo]
            if tot > winner:
                winner = tot
                winner_coord = (x+1-1, y+1-1)
    return winner_coord, winner

def p2(grid):
    winner = -100
    winner_coord = (-1, -1, -1)
    for o in range(1, 17):
        print(f"working on o: {o*2+1}x{o*2+1}")
        offsets = [(x,y) for x in range(-o,o+1) for y in range(-o,o+1)]
        for x in range(o,len(grid)-o):
            for y in range(o,len(grid)-o):
                tot = 0
                for xo, yo in offsets:
                    tot += grid[x+xo][y+yo]
                if tot > winner:
                    winner = tot
                    winner_coord = (x+1-1, y+1-1, o*2+1)
    return winner_coord, winner


g = make_grid(serial=5153, SIZE=300)
(x,y), winner = p1(g)
print(f"Part1: {x},{y}")

g = make_grid(serial=18, SIZE=300)
(x,y), winner = p2(g)
print(f"Part1: {x},{y}")
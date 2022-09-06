from copy import deepcopy
from multiprocessing.spawn import old_main_modules

with open("input.txt") as f:
    universe = [list(x.strip()) for x in f.readlines()]

def step(universe):
    new_universe = deepcopy(universe)
    w = len(new_universe[0])
    h = len(new_universe)

    # check east
    for j, y in enumerate(universe):
        for i, x in enumerate(y):
            if (x == ">") and (universe[j][(i+1)%w] == "."):
                new_universe[j][i] = "."
                new_universe[j][(i+1)%w] = ">"

    universe = deepcopy(new_universe)
    new_universe = deepcopy(universe)
    for j, y in enumerate(universe):
        for i, x in enumerate(y):
            # check weast
            if (x == "v") and (universe[(j+1)%h][i] == "."):
                new_universe[j][i] = "."
                new_universe[(j+1)%h][i] = "v"

    return new_universe


def SAME(x,y):
    for i in range(len(x[0])):
        for j in range(len(x)):
            if x[j][i] != y[j][i]:
                return False

    return True


x = 0
while x < 10_000:
    old_universe = deepcopy(universe)
    universe = step(universe)
    x += 1

    if SAME(old_universe, universe):
        print(f"part 1: {x}")
        break
from collections import defaultdict
from itertools import combinations

def in_bounds(p, N):
    if (0 <= p[0] < N) and (0 <= p[1] < N):
        return True
    else:
        return False

def part1():
    with open("input.txt", "r") as f:
        data = [x.strip() for x in f.readlines()]

    assert len(data) == len(data[0])
    N = len(data)

    world = defaultdict(set)
    for x in range(len(data)):
        for y in range(len(data)):
            if data[y][x] != ".":
                world[data[y][x]].add((x,y))

    antinodes = set()
    for frequency, antennas in world.items():
        combos = combinations(antennas, 2)
        for combo in combos:
            a, b = combo
            delta1 = (a[0] - b[0], a[1] - b[1])
            new1 = (a[0] + delta1[0], a[1] + delta1[1])
            delta2 = (b[0] - a[0], b[1] - a[1])
            new2 = (b[0] + delta2[0], b[1] + delta2[1])
            if in_bounds(new1, N):
                antinodes.add(new1)
            if in_bounds(new2, N):
                antinodes.add(new2)
            
    return len(antinodes)

def part2():
    with open("input.txt", "r") as f:
        data = [x.strip() for x in f.readlines()]

    assert len(data) == len(data[0])
    N = len(data)

    world = defaultdict(set)
    for x in range(len(data)):
        for y in range(len(data)):
            if data[y][x] != ".":
                world[data[y][x]].add((x,y))

    antinodes = set()
    for frequency, antennas in world.items():
        combos = combinations(antennas, 2)
        for combo in combos:
            a, b = combo
            delta1 = (a[0] - b[0], a[1] - b[1])
            i = 0
            while True:
                new1 = (a[0] + delta1[0]*i, a[1] + delta1[1]*i)
                i += 1
                if in_bounds(new1, N):
                    antinodes.add(new1)
                else:
                    break

            delta2 = (b[0] - a[0], b[1] - a[1])
            i = 0
            while True:
                new2 = (b[0] + delta2[0]*i, b[1] + delta2[1]*i)
                i += 1
                if in_bounds(new2, N):
                    antinodes.add(new2)
                else:
                    break
    
    return len(antinodes)

print(f"part 1: {part1()}")
print(f"part 2: {part2()}")
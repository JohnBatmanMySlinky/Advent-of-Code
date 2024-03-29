from collections import defaultdict

with open("input.txt") as f:
    data = [list(x.strip()) for x in f.readlines()]

def neighbors(data, p, path):
    x,y = p
    n = []
    for i in [1,-1]:
        # bounds check
        if (x+i < len(data[0]))&(x+i >= 0):
            # z --> E won't pass height check⌈
            if (data[y][x+i] == "E")&(data[y][x]=="z"):
                n.append((x+i,y))
            # height check
            if ord(data[y][x+i]) - ord(data[y][x]) <= 1:
                if (x+i,y) not in path:
                    n.append((x+i,y))
    for i in [1,-1]:
        if (y+i < len(data))&( y+i >= 0):
            if (data[y+i][x] == "E")&(data[y][x]=="z"):
                n.append((x, y+i))
            if ord(data[y+i][x]) - ord(data[y][x]) <= 1:
                if (x,y+i) not in path:
                    n.append((x,y+i))
    return n

def neighbors2(data, p, path):
    x,y = p
    n = []
    for i in [1,-1]:
        # bounds check
        if (x+i < len(data[0]))&(x+i >= 0):
            # z --> E won't pass height check⌈
            if (data[y][x+i] == "E")&(data[y][x]=="z"):
                n.append((x+i,y))
            # height check
            if ord(data[y][x+i]) - ord(data[y][x]) >= -1:
                if (x+i,y) not in path:
                    n.append((x+i,y))
    for i in [1,-1]:
        if (y+i < len(data))&( y+i >= 0):
            if (data[y+i][x] == "E")&(data[y][x]=="z"):
                n.append((x, y+i))
            if ord(data[y+i][x]) - ord(data[y][x]) >= -1:
                if (x,y+i) not in path:
                    n.append((x,y+i))
    return n

def p1(data):
    # find start
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] == "S":
                start = (x,y)
    data[start[1]][start[0]] = "a"

    # find end
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] == "E":
                finish = (x,y)

    log = [[0 for a in range(len(data[0]))] for b in range(len(data))]

    q = [start]
    visited = set()
    while q:
        curr = q.pop(0)
        visited.add(curr)
        for n in neighbors(data, curr, visited):
            # only update if first visit or better path distance
            if (log[n[1]][n[0]]==0) | (log[curr[1]][curr[0]] + 1 <= log[n[1]][n[0]]):
                log[n[1]][n[0]] = log[curr[1]][curr[0]] + 1
            q.append(n)
            visited.add(n)

    return log[finish[1]][finish[0]]


def p2(data):
    # find start
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] == "E":
                start = (x,y)
    data[start[1]][start[0]] = "z"

    print(f"start: {start}")

    log = [[0 for a in range(len(data[0]))] for b in range(len(data))]

    q = [start]
    visited = set()
    while q:
        curr = q.pop(0)
        visited.add(curr)
        for n in neighbors2(data, curr, visited):
            # only update if first visit or better path distance
            # if (log[n[1]][n[0]]==0) | (log[curr[1]][curr[0]] + 1 <= log[n[1]][n[0]]):
            log[n[1]][n[0]] = log[curr[1]][curr[0]] + 1
            q.append(n)
            visited.add(n)

        # print("\n")
        # for l in log:
        #     print("".join([str(x) for x in l]))
        # input()

    tmp = []
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] == "a":
                tmp.append(log[y][x])

    return min([x for x in tmp if x != 0])

print(f"part 1: {p1(data)}")
print(f"part 2: {p2(data)}")
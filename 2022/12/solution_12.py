from collections import defaultdict

with open("input.txt") as f:
    data = [list(x.strip()) for x in f.readlines()]

def neighbors(data, p, path):
    x,y = p
    n = []
    for i in [1,-1]:
        if (x+i < len(data[0]))&(x+i >= 0):
            if abs(ord(data[y][x+i]) - ord(data[y][x])) < 2:
                if (x+i,y) not in path:
                    n.append((x+i,y))
    for i in [1,-1]:
        if (y+i < len(data))&( y+i >= 0):
            if abs(ord(data[y+i][x]) - ord(data[y][x])) < 2:
                if (x,y+i) not in path:
                    n.append((x,y+i))
    return n

def p1(data):
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] == "S":
                start = (x,y)
    data[start[1]][start[0]] = "a"

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
            log[n[1]][n[0]] = log[curr[1]][curr[0]] + 1
            q.append(n)
            visited.add(n)
            
            # print(q, visited, log)
            # input()


    return log[finish[1]][finish[0]]

print(f"part 1: {p1(data)}")
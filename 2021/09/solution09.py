with open('input.txt') as f:
    dat = [x.strip() for x in f.readlines()]

from functools import reduce

def part1(dat):
    adj = [(1,0), (-1,0), (0,1), (0,-1)]
    score = 0

    for r in range(len(dat)):
        for c in range(len(dat[0])):
            check = []
            current = int(dat[r][c])
            for x,y in adj:
                if len(dat)-1 >= r+x >= 0 and len(dat[0])-1 >= c+y >= 0:
                    if int(dat[r+x][c+y]) > current:
                        check.append(True)
                    else:
                        check.append(False)

            if all(check):
                score += current + 1    

    return score

print(part1(dat))


def get_neighbors(board, current):
    neighbors = []
    adj = [(1,0), (-1,0), (0,1), (0,-1)]
    r = current[0]
    c = current[1]
    for x,y in adj:
        if len(board)-1 >= r+x >= 0 and len(board[0])-1 >= c+y >= 0:
            if board[r+x][c+y] != '9':
                neighbors.append((r+x,c+y))
    
    return neighbors


def bfs(board, start):
    visited = [start]
    queue = [start]

    while queue:
        s = queue.pop()
        
        neighbors = get_neighbors(board, s)

        for neighbor in neighbors:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
    return len(visited), visited


def part2(dat):
    score = []
    visited_all = []
    for r in range(len(dat)):
        for c in range(len(dat[0])):
            if (r,c) in visited_all or dat[r][c] == '9':
                continue
            basin_size, visited = bfs(dat,(r,c))
            score.append(basin_size)
            visited_all += visited

    ss = sorted(score, reverse=True)[:3]

    return reduce((lambda x,y: x*y), ss)


print(part2(dat))
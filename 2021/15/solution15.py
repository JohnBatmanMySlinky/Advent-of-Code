with open('input.txt') as f:
    dat = [[int(x) for x in x.strip()] for x in f.readlines()]

from collections import defaultdict
import heapq as heap

def find_neighbors(board, current):
    maxlen = len(board)-1
    x,y = current
    neighbors = []
    for i,j in [(1,0), (-1,0), (0,1), (0,-1)]:
    # for i,j in [(0,1), (1,0)]:
        if 0 <= x+i <= maxlen and 0 <= y+j <= maxlen:
            neighbors.append((x+i,y+j))
    
    return neighbors

def dijkstra(board, start):
    visited = set()
    que = []
    scores = defaultdict(lambda: float('inf'))
    scores[start] = 0
    heap.heappush(que, (board[start[1]][start[0]], start))

    while que:
        _, current = heap.heappop(que)
        visited.add(current)

        for neighbor in find_neighbors(board, current):
            if neighbor not in visited:
                score = scores[current] + board[neighbor[1]][neighbor[0]]

                if scores[neighbor] > score:
                    scores[neighbor] = score                    
                    heap.heappush(que, (score, neighbor))
    return scores[(len(board)-1, len(board)-1)]

def p2(board):
    new = []
    # ok go right
    for row in board:
        newrow = []
        for offset in range(5):
            newrow+= [x+offset-9 if x+offset > 9 else x+offset for x in row]
        new.append(newrow)

    newnew = []
    for offset in range(5):
        for row in new:
            newnew.append([x+offset-9 if x+offset > 9 else x+offset for x in row])

    return newnew

print(dijkstra(dat.copy(), (0,0)))
print(dijkstra(p2(dat), (0,0)))


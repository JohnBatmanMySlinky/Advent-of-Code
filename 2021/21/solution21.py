import sys
from collections import deque

A = int(sys.argv[1])
B = int(sys.argv[2])

def part1(A,B,N):
    q = deque(list(range(1,N+1))*20)

    Ascore = 0
    Bscore = 0
    i = 0

    while q:
        for _ in range(3):
            A += q.popleft()
        if A > 10:
            A %= 10
        if A == 0:
            A = 10
        Ascore += A
        if Ascore >= 1000:
            return (i*6+3) * Bscore

        for _ in range(3):
            B += q.popleft()
        if B > 10:
            B %= 10
        if B == 0:
            B = 10
        Bscore += B
        if Bscore >= 1000:
            return (i*6+6) * Ascore

        i += 1
# print(part1(A,B,100))


from collections import defaultdict

moves = [(x,y,z) for x in [1,2,3] for y in [1,2,3] for z in [1,2,3]]
dist = defaultdict(int)
for move in moves: 
    dist[sum(move)] += 1
# a pos, b pos, a score, b score
universes = defaultdict(int, {(x,y,z,a):0 for x in range(1,11) for y in range(1,11) for z in range(0,21) for a in range(0,21)})
universes[(A,B,0,0)]=1

log = [0,0]
i = 0
while universes:
    new_universes = defaultdict(int)
    for universe, population in universes.items():
        if population > 0:
            for ka, va in dist.items():
                apos = (universe[0]+ka-1)%10+1
                ascore = universe[2]+apos
                if ascore >= 21:
                    log[0] += population * va
                    continue

                for kb, vb in dist.items():
                    bpos = (universe[1]+kb-1)%10+1
                    bscore = universe[3] + bpos
                    if bscore >= 21:
                        log[1] += population * vb * va
                    else:
                        new_universes[(apos, bpos, ascore, bscore)] += population * va * vb
    universes = new_universes

print(max(log))









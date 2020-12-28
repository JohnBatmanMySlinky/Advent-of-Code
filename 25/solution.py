import sys

dat = [x.strip('\n') for x in sys.stdin]

card = int(dat[0])
door = int(dat[1])
subj = 7
m = 20201227

# solve
def solve(targ, start, subj, m):
    out = 0
    while start != targ:
        out += 1
        start = start * subj % m
    return(out)

def handshake(card, door, cloop, dloop, m):
    d_handshake = 1
    for _ in range(cloop):
        d_handshake = d_handshake * door % m

    c_handshake = 1
    for _ in range(dloop):
        c_handshake = c_handshake * card % m

    if d_handshake == c_handshake:
        return(d_handshake)
    else:
        return(False)


cloop = solve(card, 1, subj, m)
dloop = solve(door, 1, subj, m)
print('part1: ' + str(handshake(card, door, cloop, dloop, m)))


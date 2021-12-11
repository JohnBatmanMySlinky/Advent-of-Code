with open('input.txt') as f:
    raw = [x.strip() for x in f.readlines()]
    dat = []
    for r in raw:
        row = []
        for i in r:
            row.append(int(i))
        dat.append(row)

def glow_up(state, r, c):
    new_mask = []
    for x, y in [(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1)]:
        if (0 <= r + x <= len(state) - 1) and (0 <= c + y <= len(state) - 1):
            state[r + x][c + y] += 1

            if state[r+x][c+y] == 10:
                new_mask.append((r+x,c+y))
    return state, new_mask

def cycle(state, flashes):
    mask = []
    for r in range(len(state)):
        for c in range(len(state)):
            state[r][c] += 1

            if state[r][c] == 10:
                mask.append((r,c))

    while mask:
        r,c = mask.pop()
        state, new_mask = glow_up(state, r, c)
        mask += new_mask


    for r in range(len(state)):
        for c in range(len(state)):
            if state[r][c] > 9:
                flashes += 1
                state[r][c] = 0

    return state, flashes


def part1(dat,N):
    flashes = 0
    state = dat.copy()

    for i in range(N):
        state, flashes = cycle(state, flashes)

    return flashes

def check_all(state):
    tot = 0
    for x in state:
        tot += sum(x)
    return tot

def part2(dat):
    state = dat.copy()
    flashes = 0
    i = 0
    while i < 1000:
        i += 1
        state, _ = cycle(state, flashes)

        if check_all(state)==0:
            return i

print(part1(dat,100))
print(part2(dat)+100)

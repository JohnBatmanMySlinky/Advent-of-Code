import re
with open("input.txt") as f:
    tmp = [x.strip() for x in f.readlines()]
    tree = dict()
    rate = dict()
    for each in tmp:
        valve = each.split()[1]
        r = int(re.findall(r'=\d+', each)[0][1:])
        valves = re.findall(r'valve.+', each.split(";")[1])[0].replace(',', '').split(' ')[1:]
        tree[valve] = valves
        rate[valve] = r

def p1(tree, rate, guess):
    # BFS
    # cumrate, curr, open, path taken so far
    stats = [[0, 'AA', set(), []]]
    for m in range(30):
        # if this requires memoization i quit
        # can we just toss the shitty ones?
        if len(stats) > guess:
            stats.sort()
            stats = stats[-guess:]
        newstats = []
        for cumrate, curr, opn, pth in stats:            
            # spend a minute opening
            # if not already open & dont open if no rate
            if (curr not in opn) & (rate[curr] > 0):
                newstats.append([
                    cumrate + sum([rate[o] for o in opn]),
                    curr,
                    opn | {curr},
                    pth
                ])
            # spend a minute not opening and instead traveling
            for each in tree[curr]:
                    newstats.append([
                        cumrate + sum([rate[o] for o in opn]),
                        each,
                        opn.copy(),
                        pth + [curr]
                    ])
        stats = newstats[:]
        # print(stats)
        # print(m)
        # input()
    stats.sort()
    return stats[-1][0]
print(f"part 1: {p1(tree, rate, 500)}")
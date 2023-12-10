def parse():
    with open("input.txt", "r") as f:
        raw = [list(map(int,x.strip().split(" "))) for x in  f.readlines()]
    return raw


def p1():
    data = parse()
    score = 0
    for line in data:
        diffs = [line]
        while any([x != 0 for x in diffs[-1]]):
            diffs.append([x-y for x,y in zip(diffs[-1][1:], diffs[-1][:-1])])

        # grow
        for i in reversed(range(1,len(diffs))):
            diffs[i-1].append(diffs[i-1][-1] + diffs[i][-1])

        score += diffs[0][-1]
    return score

def p2():
    data = parse()
    score = 0
    for line in data:
        diffs = [line]
        while any([x != 0 for x in diffs[-1]]):
            diffs.append([x-y for x,y in zip(diffs[-1][1:], diffs[-1][:-1])])

        # shrink
        for i in reversed(range(1,len(diffs))):
            diffs[i-1] = [diffs[i-1][0] - diffs[i][0]] + diffs[i-1]

        score += diffs[0][0]
    return score

a1 = p1()
print(f"Part 1: {a1}")
a2 = p2()
print(f"Part 2: {a2}")
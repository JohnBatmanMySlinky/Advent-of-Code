from collections import Counter, defaultdict
from itertools import tee

def pairwise(iterable):
    # pairwise('ABCDEFG') --> AB BC CD DE EF FG
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

with open('input.txt') as f:
    raw = [x.strip() for x in f.readlines()]
    template = raw[0]
    dat = {x.split(' -> ')[0]:x.split(' -> ')[1] for x in raw[2:]}

def part1(old, rules, cycles, verbose=False):
    for i in range(cycles):
        new = ""
        for pair in pairwise(old):
            new += pair[0] + rules[pair[0]+pair[1]]
        old = new + old[-1]

    counts = Counter(old).most_common()
    return counts[0][1] - counts[-1][1]

def part2(start, rules, cycles):
    old = defaultdict(int)
    for pairs in pairwise(start):
        old[pairs] += 1

    for i in range(cycles):
        new = defaultdict(int)
        for pair in old.keys():
            new[pair[0] + rules[pair[0] + pair[1]]] += old[pair]
            new[rules[pair[0] + pair[1]] + pair[1]] += old[pair]
        old = new.copy()

        # print(old)
        # print(sum(old.values()))
        # input()

    counter = defaultdict(int)
    # omg double counting
    counter[start[0]] += 1
    counter[start[-1]] += 1
    for k,v in old.items():
        counter[k[0]] += v
        counter[k[1]] += v
    

    return int((max(counter.values()) - min(counter.values()))/2)


print(part1(template, dat, 10))

print(part2(template, dat, 40))







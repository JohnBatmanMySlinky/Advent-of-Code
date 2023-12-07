import sys

INPUT = sys.argv[1]

def parse():
    with open(INPUT, "r") as f:
        data = [x.strip() for x in f.readlines()]
    seeds = [int(i) for i in data.pop(0).split(": ")[1].split(" ")]
    _ = data.pop(0)
    struct = []
    tmp = []
    for maps in data:
        if maps.find(":") > 0:
            continue
        elif maps == "":
            struct.append(tmp)
            tmp = []
        else:
            tmp.append([int(i) for i in maps.split(" ")])
    struct.append(tmp)
    return seeds, struct

def p1(seeds, maps):

    log = {}
    for seed in seeds:
        seedlog = [seed]
        for chunk in maps:
            found = False
            curr = seedlog[-1]
            for dest, inp, r in chunk:
                if curr in range(inp, inp+r):
                    seedlog.append(curr+dest-inp)
                    found = True
                if found:
                    break
            if found == False:
                seedlog.append(curr)
        log[seed] = seedlog


    lowest = 999999999999999999999
    for k,v in log.items():
        if v[-1] < lowest:
            lowest = v[-1]
    return lowest

def p2():
    seeds, maps = parse()
    seedranges = [range(x,x+y) for x,y in zip(seeds[::2], seeds[1::2])]

    upper_bound = 0
    for seed in seeds[::2]:
        answer = p1([seed], maps)
        if (answer > upper_bound) and any([answer in x for x in seedranges]):
            upper_bound = answer

    # we can use the even number seeds to get an upper bound
    # then solve in reverse? 500M ok so that's rough but doable?
    
    winner = upper_bound
    for seed in range(0,500_000_000):
        seedlog = [seed]
        for chunk in reversed(maps):
            found = False
            curr = seedlog[-1]
            for dest, inp, r in chunk:
                if curr-dest+inp in range(inp, inp+r):
                    seedlog.append(curr-dest+inp)
                    found = True
                if found:
                    break
            if found == False:
                seedlog.append(curr)
        if any([seedlog[-1] in seedrange for seedrange in seedranges]):
            if seedlog[-1] < winner:
                winner = seedlog[-1]
    return winner




seeds, maps = parse()
a1 = p1(seeds, maps)
print(f"Part 1: {a1}")
a2 = p2()
print(f"part 2: {a2}")
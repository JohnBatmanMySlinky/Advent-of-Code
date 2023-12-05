def parse():
    with open("input.txt", "r") as f:
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

def p1():
    seeds, maps = parse()

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

    log = {}
    for i, seedrange in enumerate(seedranges):
        print(f"P2: {i+1}/{len(seedranges)}")
        for seed in seedrange:
            seedlog = [seed]
            for chunk in maps:
                found = False
                curr = seedlog[-1]
                for dest, inp, r in chunk:
                    if curr in range(inp, inp+r):
                        seedlog.append(curr+dest-inp)
                        found = True
                if found == False:
                    seedlog.append(curr)
            log[seed] = seedlog


    lowest = 999999999999999999999
    for k,v in log.items():
        if v[-1] < lowest:
            lowest = v[-1]
    return lowest

a1 = p1()
print(f"Part 1: {a1}")
a2 = p2()
print(f"part 2: {a2}")
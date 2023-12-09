def parse1():
    with open("input.txt", "r") as f:
        raw = f.readlines()

    data = []
    for line in raw:
        for x in reversed(range(2,11)):
            line = line.replace(" "*x, " "*(x-1))
        line = line.split(" ")
        data.append([int(x) for x in line[1:]])

    return data

def p1():
    time, distance = parse1()

    log = []
    for t, d in zip(time, distance):
        combos = 0
        for x in range(0,t+1):
            score = x * (t-x)
            if score > d:
                combos += 1

        log.append(combos)

    # heinous
    if len(log) == 3:
        return log[0] * log[1] * log[2]
    else:
        return log[0] * log[1] * log[2] * log[3]
    
def parse2():
    with open("input.txt", "r") as f:
        raw = f.readlines()

    data = []
    for line in raw:
        for x in reversed(range(1,11)):
            line = line.replace(" "*x, " "*(x-1))
        line = line.split(":")
        data.append([int(x) for x in line[1:]])
    return data

def p2():
    time, distance = parse2()

    log = []
    for t, d in zip(time, distance):
        combos = 0
        for x in range(0,t+1):
            score = x * (t-x)
            if score > d:
                combos += 1

        log.append(combos)

    return log[0]

a1 = p1()
print(f"Part 1: {a1}")
a2 = p2()
print(f"Part 2: {a2}")
import math

with open("input.txt", "r") as f:
    lines = f.readlines()[0].split(",")
    data = [(int(x.split("-")[0]), int(x.split("-")[1])) for x in lines]

def generate_invalid1(min_dig, max_dig):
    min_dig = math.ceil(min_dig / 2) * 2
    max_dig = (max_dig // 2) * 2

    invalid = set()

    for x in range(min_dig, max_dig+1):
        if x % 2 != 0:
            continue
        lower = 10**(x//2-1)
        upper = 10**(x//2)
        for i in range(lower, upper):
            invalid.add(int(str(i)*2))

    return invalid

def p1(data):
    maxx = max([len(str(y)) for _,y in data])

    invalids = generate_invalid1(2,maxx)
    tot = 0
    for lower, upper in data:
        for invalid in invalids:
            if lower <= invalid <= upper:
                tot += invalid
    return tot

def generate_invalid2(max_dig):
    invalid = set()
    for n_digits in range(1, max_dig//2+1):
        for repeated in range(2, max_dig+1):
            if repeated == 1:
                continue
            if n_digits * repeated > max_dig:
                continue
            lower = 10**(n_digits-1)
            upper = 10**(n_digits)
            for i in range(lower, upper):
                tmp = int(str(i)*repeated)
                invalid.add(tmp)         
    return invalid

def p2(data):
    maxx = max([len(str(y)) for _,y in data])

    invalids = generate_invalid2(maxx)
    tot = 0
    for lower, upper in data:
        for invalid in invalids:
            if lower <= invalid <= upper:
                tot += invalid
    return tot

answer = p1(data)
print(f"part1: {answer}")

answer = p2(data)
print(f"part2: {answer}")


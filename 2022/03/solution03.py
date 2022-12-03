with open("input.txt") as f:
    dat = [x.strip() for x in f.readlines()]
    

def p1(dat):
    lengths = [len(x)//2 for x in dat]
    data = [set(d[:l]).intersection(set(d[l:])) for l,d in zip(lengths, dat)]
    winner = 0
    for ruckasck in data:
        for thing in ruckasck:
            winner += score(thing)
    return winner

def p2(dat):
    winner = 0
    for x in range(0,len(dat),3):
        common = set(dat[x]).intersection(set(dat[x+1])).intersection(set(dat[x+2]))
        for thing in common:
            winner += score(thing)
    return winner

def score(x):
    if x.isupper():
        return ord(x)-38
    else:
        return ord(x)-96


print(f"part1: {p1(dat)}")
print(f"part1: {p2(dat)}")
from collections import Counter

with open(r"input.txt","r") as f:
    raw = [x.strip("\n").split("-") for x in f.readlines()][0]
    raw = [int(x) for x in raw]
    
def check_increasing(pwd):
    tmp = [x for x in str(pwd)]
    return all([int(y)>=int(x) for (x,y) in zip(tmp[:-1],tmp[1:])])

def check_double(pwd):
    tmp = set([x for x in str(pwd)])
    return len(tmp) < len(str(pwd))

def check_larger_group(pwd):
    tmp = Counter(str(pwd))
    return any([x==2 for x in tmp.values()])

p1 = 0
for pwd in range(raw[0],raw[1]+1):
    if check_increasing(pwd):
        if check_double(pwd):
            p1 += 1
print("part1: {}".format(p1))


p2 = 0
for pwd in range(raw[0],raw[1]+1):
    if check_increasing(pwd):
        if check_larger_group(pwd):
            p2 += 1
print("part2: {}".format(p2))
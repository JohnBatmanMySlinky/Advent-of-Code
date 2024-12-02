from copy import deepcopy

def p1():
    with open("input.txt", "r") as f:
        data = []
        for line in f.readlines():
            data.append(list(map(int,line.strip().split(" "))))

    OK = 0
    for line in data:
        new = []
        for a,b in zip(line[1:], line[:-1]):
            new += [a-b]
        assert len(new) == len(line)-1
        if all([x in [-1,-2,-3] for x in new]) or all([x in [1,2,3] for x in new]):
            OK += 1

    return OK

def p2():
    with open("input.txt", "r") as f:
        data = []
        for line in f.readlines():
            data.append(list(map(int,line.strip().split(" "))))

    OK = 0
    for line in data:
        maybe = 0
        for i in range(len(line)):
            newnew = deepcopy(line)
            newnew.pop(i)
            new = []
            for a,b in zip(newnew[1:], newnew[:-1]):
                new += [a-b]
            assert len(new) == len(newnew)-1
            if all([x in [-1,-2,-3] for x in new]) or all([x in [1,2,3] for x in new]):
                maybe += 1
        if maybe > 0:
            OK += 1

    return OK

print(f"part1: {p1()}")
print(f"part1: {p2()}")
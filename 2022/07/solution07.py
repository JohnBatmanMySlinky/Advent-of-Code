from collections import defaultdict

with open("input.txt") as f:
    data = [x.strip().split() for x in f.readlines()]

def create_tree(data):
    tree = defaultdict(int)
    i = 0
    key = []
    for dat in data:
        if dat[0] == "$":
            if dat[1] == "cd":
                if dat[2] == "..":
                    key.pop(-1)
                else:
                    key.append(dat[2])
            elif dat[1] == "ls":
                pass
            else:
                assert False
        elif dat[0].isnumeric():
            for i in range(len(key)): # this fucking line >:(
                tree[tuple(key[:i+1])] += int(dat[0])
        elif dat[0] == "dir":
            pass
        else:
            assert False
    return tree
        
def p1(data):
    tree = create_tree(data)
    winner = 0
    for k,v in tree.items():
        if v <= 100_000:
            winner += v
    return winner

def p2(data):
    tree = create_tree(data)

    system = 70_000_000
    needed = 30_000_000
    update =  -1 * (system - tree[('/',)] - needed)
    winner = min([v for k,v in tree.items() if v > update])
    return winner


print(f"part 1: {p1(data)}")
print(f"part 2: {p2(data)}")
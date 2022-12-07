from collections import defaultdict

with open("input.txt") as f:
    data = [x.strip() for x in f.readlines()]

def pop(s):
    return "||" + "||".join(s.split("||")[1:-1])

def create(data):
    tree = dict()
    i = 0
    key = ""
    while i-1 < len(data):
        if data[i] == "$ ls":
            i += 1
            while data[i][0] != "$":
                a,b = data[i].split(' ')
                if a.isnumeric():
                    tree[key+"||"+b] = a
                i += 1
                if i == len(data):
                    return tree
        elif data[i][:4] == "$ cd":
            a, b, c = data[i].split(" ")
            if c == "..":
                key = pop(key)
            elif c == "/":
                key = "/"
            else:
                key += "||" + c
            i += 1

def p1(data):
    tree = create(data)
    folder_set = defaultdict(int)
    for k, v in tree.items():
        for kk in k.split("||")[1:-1]:
            folder_set[kk] += int(v)
    winner = 0
    for k,v in folder_set.items():
        if v <= 100_000:
            winner += v
    return winner


print(f"part 1: {p1(data)}")
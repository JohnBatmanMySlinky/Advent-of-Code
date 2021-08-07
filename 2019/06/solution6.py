with open(r"input.txt","r") as f:
    raw = [x.rstrip().split(")") for x in f.readlines()]

from collections import defaultdict

tree = defaultdict(list)
universe = set()
for x,y in raw:
    tree[x].append(y)
    universe.add(x)
    universe.add(y)

# slow but I don't feel like using recursion to calc node depth at 2am
part1_fin = 0
for each in universe:
    parent = each
    part1 = 0
    while parent != 'COM':
        part1 += 1
        parent = [k for (k,v) in tree.items() if parent in v][0]
    part1_fin += part1

print(part1_fin)
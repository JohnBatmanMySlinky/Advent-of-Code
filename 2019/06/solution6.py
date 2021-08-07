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

print('part1: {}'.format(part1_fin))


flipped = defaultdict(list)
root = 'YOU'
queue = []
#init flipped
for k,v in tree.items():
    if root in v:
        v.remove(root)
        flipped[root].append(k)
        queue.append(k)

i = 0
while queue:
    tmp = queue.pop(0)
    for k,v in tree.items():
        if tmp == k:
            flipped[tmp] += v
            queue += v
            tree[k] = []
        elif tmp in v:
            flipped[tmp].append(k)
            queue.append(k)
            v.remove(tmp)

# part 2
# modified dfs
visited = set()
def dfs(visited, flipped, node, goal, depth):
    if node not in visited:
        depth += 1
        if node == goal:
            print('part2: {}'.format(depth-3))
        visited.add(node)
        for neighbor in flipped[node]:
            dfs(visited, flipped, neighbor, goal, depth)

dfs(visited, flipped, 'YOU', 'SAN', 0)

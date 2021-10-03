from copy import deepcopy

with open('input.txt') as f:
    dat = [x.strip() for x in f.readlines()]

tree = {}
for i,y in enumerate(dat):
    for j,x in enumerate(y):
        if x != '#':
            tree[(j,i)] = x

pos = [k for k,v in tree.items() if v == '@'][0]
visited = []
queue = []

def generate_next(pos, move):
    if move == 1:
        out = (pos[0] + 1, pos[1])
    elif move == 2:
        out = (pos[0] - 1, pos[1])
    elif move == 3:
        out = (pos[0], pos[1] + 1)
    elif move == 4:    
        out = (pos[0], pos[1] - 1)
    return out
    
ascii_lower = [chr(x) for x in range(97,123)]

def find_next_keys(tree, current):
    visited = [current]
    queue = [(current, 1)]
    keys = {}
    
    while queue:
        s, d = queue.pop(0)
        for neighbor in [generate_next(s,x) for x in range(1,5)]:
            if neighbor in tree.keys():
                if neighbor not in visited:
                    visited.append(neighbor)
                    if tree[neighbor] == '.':
                        queue.append((neighbor, d+1))
                    if tree[neighbor] in ascii_lower:
                        keys[tree[neighbor]] = [neighbor, d]
    return keys


# def traverse(tree, symbol, depth, solutions, paths):
#     pos = [k for k,v in tree.items() if v == symbol][0]
#     tree[pos] = '.'
#     if symbol != '@':
#         if symbol.upper() in tree.values():
#             upper_pos = [k for k,v in tree.items() if v == symbol.upper()][0]
#             tree[upper_pos] = '.'
#         elif all([x=='.' for x in tree.values()]):
#             solutions.append(depth)
#             print(solutions)
#             print(depth)
#         else:
#             pass
#     neighbors = find_next_keys(tree, pos)
#     if neighbors:
#         for neighbor in neighbors.keys():
#             print(neighbor, depth+neighbors[neighbor][1], tree)
#             input()
#             traverse(tree.copy(), neighbor, depth+neighbors[neighbor][1], solutions)


#     return min(solutions)


def traverse(tree, symbol, depth, solutions, visited):
    pos = [k for k,v in tree.items() if v == symbol][0]
    tree[pos] = '.'
    if symbol != '@':
        if symbol.upper() in tree.values():
            upper_pos = [k for k,v in tree.items() if v == symbol.upper()][0]
            tree[upper_pos] = '.'
        elif all([x=='.' for x in tree.values()]):
            solutions.append(depth)
#             print(solutions)
#             print(visited)
#             print(depth)
        else:
            pass
    neighbors = find_next_keys(tree, pos)
    visited.append(symbol)
    if neighbors:
        for neighbor in [x for x in neighbors.keys() if x not in visited]:
#             print(neighbor, depth+neighbors[neighbor][1], tree, visited)
#             input()
            traverse(tree.copy(), neighbor, depth+neighbors[neighbor][1], solutions, visited + [neighbor])


    return min(solutions)

print(traverse(tree, '@', 0, [], []))

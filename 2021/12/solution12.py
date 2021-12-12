from collections import defaultdict

graph = defaultdict(list)

with open('input.txt') as f:
    raw = [x.strip().split('-') for x in f.readlines()]
    for x,y in raw:
        graph[x].append(y)
        graph[y].append(x)

def part1(visited, graph, current):
    if current == 'end':
        return 1
    if current.islower() and current in visited:
        return 0

    if current.islower():
        visited = visited.copy()
        visited.add(current)

    i = 0
    for neighbor in graph[current]:
        i += part1(visited, graph, neighbor)

    return i

print(part1(set(), graph, 'start'))

def part2(visited, graph, current, dupe):
    if current == 'end': # if end success
        return 1
    if current == 'start' and visited: # if start and have visited sum, exit
        return 0

    # additional exit criteria
    # if current is lower and we've seen it, check dupe flag, continue or exit
    if current.islower() and current in visited:
        if not dupe:
            dupe = current
        else:
            return 0

    # same
    if current.islower():
        visited = visited.copy()
        visited.add(current)

    i = 0
    for neighbor in graph[current]:
        i += part2(visited, graph, neighbor, dupe)

    return i

print(part2(set(), graph, 'start', None))
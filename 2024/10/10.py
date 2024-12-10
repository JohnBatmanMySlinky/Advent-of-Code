def valid(maybe, graph):
    x,y = maybe
    return 0 <= x < len(graph) and 0 <= y < len(graph)

def neighbors(graph, current):
    x, y = current
    i = graph[y][x]
    neighbors = []
    for xo,yo in [(1,0), (-1,0), (0,1), (0,-1)]:
        if valid((x+xo, y+yo), graph):
            if graph[y+yo][x+xo] == i + 1:
                neighbors.append((x+xo, y+yo))
    return neighbors

def dfs_inner(graph, start, results):
    print(f"recursing - {results}")
    for neighbor in neighbors(graph, start):
        dfs_inner(graph, neighbor, results + [neighbor])
    return results

def dfs_outer(graph, start, results):
    print(start)
    full_results = []
    for neighbor in neighbors(graph, start):
        results.extend(dfs_inner(graph, neighbor, results + [neighbor]))
        if results:
            x,y = results[-1]
            if graph[y][x] == 9:
                print(f"boop - {results}")
                full_results.append(results)

    return full_results

def part1():
    with open("input.txt", "r") as f:
        data = [list(map(int,x.strip())) for x in f.readlines()]

    assert len(data) == len(data[0])
    starts = set()
    for x in range(len(data)):
        for y in range(len(data)):
            if data[y][x] == 0:
                starts.add((x,y))
    
    for start in starts:
        path = dfs_outer(data, start, [])
        print(path)
        assert False

print(f"part 1: {part1()}")
with open(r"input.txt","r") as f:
    raw = [x.strip("\n").split(",") for x in f.readlines()]
    
def unit_mapper(point, direction):
    if direction == 'U':
        new = [point[0], point[1], point[2] + 1]
    elif direction == 'D':
        new = [point[0], point[1], point[2] - 1]
    elif direction == 'R':
        new = [point[0], point[1] + 1, point[2]]
    elif direction == 'L':
        new = [point[0], point[1] - 1, point[2]]
    else:
        assert 0 > 0 
    
    return new

def manhattan_distance(point):
    return abs(point[0]) + abs(point[1])
    
all_points = []
for coords in raw:
    points = [[0,0,0]]
    x = 0
    for step in coords:
        direction = step[0]
        units = int(step[1:])
        for i in range(units):
            x += 1
            points.append(unit_mapper(points[-1], direction))
            points[-1][0] = x
    all_points.append(points)

# part 1 removing step count to get overlap via sets then manhattan distance
all_points_manhattan = []
for x in all_points:
    tmp = []
    for y in x:
        tmp.append(tuple(y[1:]))
    all_points_manhattan.append(tmp)
overlap = list(set(all_points_manhattan[0]) & set(all_points_manhattan[1]))
print("part1: {}".format(min([manhattan_distance(x) for x in overlap if manhattan_distance(x)>0])))

# given overlapping coords go back and find step count for those coords.
p2 = 1_000_000
for o in overlap:
    a_steps = [x[0] for x in all_points[0] if o == tuple(x[1:]) and x[0]>0]
    b_steps = [x[0] for x in all_points[1] if o == tuple(x[1:]) and x[0]>0]
    if len(a_steps)>0 and len(b_steps)>0:
        if a_steps[0]+b_steps[0] < p2:
            p2 = a_steps[0]+b_steps[0]
print("part2: {}".format(p2))
with open("input.txt") as f:
    data = [list(map(int,x.strip().split(','))) for x in f.readlines()]

def p1(data):
    cubes = dict()
    for x, y, z in data:
        cubes[(x,y,z)] = 6
        for (xx,yy,zz), v in cubes.items():
            if sorted(abs(a-b) for a,b in [(x,xx), (y,yy), (z,zz)])==[0,0,1]:
                cubes[(x,y,z)] -= 1
                cubes[(xx,yy,zz)] -= 1
    return sum(cubes.values())

def add(a,b):
    return [a[0]+b[0], a[1]+b[1], a[2]+b[2]]

def in_bounds(a):
    if min(a) < MIN or max(a) > MAX:
        return False
    else:
        return True

MIN = 0
MAX = 20

def p2(data):
    # build a cube around lava
    # find air cubes on the outisde using BFS
    # using set math to find inside air cubes
    # all_cubes = lava cubes + outside air cubes - inside air cubes
    # once you have inside aircubes it is p1(lava cubes) - p1(inside air cubes)
    q = [[0,0,0]]
    outsideair = []
    while q:
        current = q.pop(0)
        for each in [[-1,0,0], [1,0,0], [0,-1,0], [0,1,0], [0,0,-1], [0,0,1]]:
            new = add(current,each)
            if in_bounds(new) & (new not in data) & (new not in outsideair):
                q.append(new)
                outsideair.append(new)
    
    inside_air = []
    for x in range(MIN,MAX+1):
        for y in range(MIN,MAX+1):
            for z in range(MIN,MAX+1):
                if ([x,y,z] not in outsideair) & ([x,y,z] not in data):
                    inside_air.append([x,y,z])

    part1 = p1(data)

    cubes = dict()
    for x, y, z in inside_air:
        cubes[(x,y,z)] = 6
        for (xx,yy,zz), v in cubes.items():
            if sorted(abs(a-b) for a,b in [(x,xx), (y,yy), (z,zz)])==[0,0,1]:
                cubes[(x,y,z)] -= 1
                cubes[(xx,yy,zz)] -= 1
    return part1 - sum(cubes.values())
    

    


    



print(f"part 1: {p1(data)}")
print(f"part 2: {p2(data)}")
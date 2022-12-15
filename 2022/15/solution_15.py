import re

with open("input.txt") as f:
    data = [list(map(int,re.findall(r'(-\d+|\d+)',x))) for x in f.readlines()]

def distance(a, b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

def bounds(data):
    x = []
    y = []
    for Sx, Sy, Bx, By in data:
        x.append(Sx)
        x.append(Bx)
        y.append(Sy)
        y.append(By)
    return min(x), max(x), min(y), max(y)

def p1(data,y):
    winner = 0
    minx, maxx, miny, maxy = bounds(data)
    # I thought I was smart by getting the bounds
    # goddamit
    # I was essentially bounding radii not circumference >:(
    for i,x in enumerate(range(minx-3_000_000,maxx+3_000_000)):
        seenby = 0
        for sx, sy, bx, by in data:
            if (x,y) == (bx,by):
                pass
            else:
                current_distance = distance([x,y], [sx, sy])
                sensor_distance  = distance([bx,by], [sx, sy])
                if current_distance <= sensor_distance:
                    seenby += 1
                    break
        if seenby>0:
            winner += 1
        # if i % 10_000 == 0:
        #     print(f"{i/len(range(minx-3_000_000,maxx+3_000_000)):,.2%}")
        #     print(f"{winner:,}")
    return winner

def p2(data):
    # need to find place where four radii+1 intersect then check it aint contained by anything
    # also needing parallel lines
    sidesa = []
    sidesb = []
    for sx, sy, bx, by in data:
        r = distance([bx,by], [sx, sy])
        sidesa.append(sy-sx-r-1)
        sidesa.append(sy-sx+r+1)
        sidesb.append(sy+sx-r-1)
        sidesb.append(sy+sx+r+1)

    # parallels only
    sidesa = [a for a in sidesa if sidesa.count(a)==2]
    sidesb = [b for b in sidesb if sidesb.count(b)==2]

    for aa in sidesa:
        for bb in sidesb:
            x = (bb-aa)//2
            y = (bb+aa)//2
            if (x in range(0,4_000_001))&(y in range(0, 4_000_001)):
                winner = True
                for sx, sy, bx, by in data:
                    d1 = distance([x, y], [sx, sy])
                    d2 = distance([sx, sy], [bx, by])
                    if d1 <= d2:
                        winner = False
                if winner:
                    return 4_000_000*x+y
     
# print(f"part 1: {p1(data, 2_000_000)}")
print(f"part 2: {p2(data)}")
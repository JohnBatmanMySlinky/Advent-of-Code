with open('input.txt') as f:
    dat = []
    for x in [x.strip().split(' -> ') for x in f.readlines()]:
        a = [int(i) for i in x[0].split(',')]
        b = [int(i) for i in x[1].split(',')]
        dat.append([a,b])

from collections import defaultdict

def part1(dat):
    coords = defaultdict(int)
    for pair in dat:
        start = pair[0]
        end = pair[1]

        # if x coords same
        if start[0] == end[0]:
            shuffle = sorted([start[1], end[1]])
            for x in range(shuffle[0], shuffle[1]+1):
                coords[(start[0],x)] += 1
        # if y coords same
        elif start[1] == end[1]:
            shuffle = sorted([start[0], end[0]])
            for x in range(shuffle[0], shuffle[1] + 1):
                coords[(x,start[1])] += 1
        # DIAGONAL
        else:
            # start from coord with min x
            if start[0] < end[0]:
                a = start; b = end
            else:
                b = start; a = end

            # sloping which way
            if a[1] < b[1]:
                step = 1
            else:
                step = -1

            for x in range(0,b[0]-a[0]+1):
                coords[(a[0]+x, a[1]+x*step)] += 1

    answer = 0
    for v in coords.values():
        if v > 1:
            answer += 1

    return answer


print(part1(dat))


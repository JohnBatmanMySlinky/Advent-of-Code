with open(r"input.txt","r") as f:
    dat = [x.strip() for x in f.readlines()]
    dat = [x.split(' ') for x in dat]


dirdict = {
    'forward': [1,0,0],
    'down': [0,1,1],
    'up': [0,-1,-1],
}

def part1(dat):
    coord = [0,0]
    for d,a in dat:
        for i in [0,1]:
            coord[i] += dirdict[d][i] * int(a)
    return coord[0]*coord[1]
print(part1(dat))


def part2(dat):
    coord = [0,0,0]
    for d,a in dat:
        for i in [0,2]:
            coord[i] += dirdict[d][i] * int(a)
        if d == 'forward':
            coord[1] += coord[2] * int(a)
    return coord[0]*coord[1]
print(part2(dat)) 
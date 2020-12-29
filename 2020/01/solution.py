with open(r"input.txt","r") as f:
    dat = [int(x[:-1]) for x in f.readlines()]

# dat = [1721, 979, 366, 299, 675, 1456]

def part1(ls, targ):
    for i,x in enumerate(ls):
        for y in ls[i:]:
            if x + y == targ:
                return(x*y)

def part2(ls, targ):
    for i,x in enumerate(ls):
        for j,y in enumerate(ls[i+1:]):
            for z in ls[i+y+2:]:
                if x + y + z == targ:
                    return(x*y*z)

print(part1(dat, 2020))
print(part2(dat, 2020))

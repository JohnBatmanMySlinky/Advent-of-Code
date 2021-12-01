with open(r"input.txt","r") as f:
    dat = [int(x.strip()) for x in f.readlines()]


def part1(dat):
    return sum([y>x for x,y in zip(dat[:-1], dat[1:])])
print(part1(dat))


def part2(dat):
    counter = 0
    for x in range(len(dat)-3):
        counter += sum(dat[x+1:x+3+1]) > sum(dat[x:x+3])
    return counter

print(part2(dat))
with open(r"input.txt","r") as f:
    raw = [x.split(",") for x in f.readlines()][0]
    raw = [int(x) for x in raw]

for x in range(100):
    for y in range(100):

        dat = raw.copy()
        dat[1] = x
        dat[2] = y

        pos = 0
        while True:
            op = dat[pos]
            a,b,c = dat[pos+1], dat[pos+2], dat[pos+3]

            if op == 1:
                dat[c] = dat[a] + dat[b]
                pos += 4
            elif op == 2:
                dat[c] = dat[a] * dat[b]
                pos += 4
            elif op == 99:
                if x == 12 and y == 2:
                    print("part1: {}".format(dat[0]))
                elif dat[0] == 19690720:
                    print("part2: {}".format(100*x+y))

                break
            else:
                assert 0 > 0 


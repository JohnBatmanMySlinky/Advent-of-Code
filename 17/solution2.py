import sys

dat = [[[list(x.strip('\n')) for x in sys.stdin]]]

def play(space):
    # get size of current grid
    xdim = len(space[0][0][0])
    ydim = len(space[0][0])
    zdim = len(space[0])
    wdim = len(space)
    
    cnt = 0
    
    # build new grid expanding x and y by 1 dimension either way (2 total)
    neww = []
    for w in range(wdim+2):
        newz = []
        for z in range(zdim+2):
            newy = []
            for y in range(ydim+2):
                newx = []
                for x in range(xdim+2):

                    # for a given point find neighbors across all dimensions
                    neighbors = []
                    for d in range(-1,2,1):                   # w
                        for a in range(-1,2,1):               # z
                            for b in range(-1,2,1):           # y
                                for c in range(-1,2,1):       # x
                                    if d == a == b == c == 0:
                                        continue
                                    wcheck = w+d-1 in range(wdim)
                                    zcheck = z+a-1 in range(zdim)
                                    ycheck = y+b-1 in range(ydim)
                                    xcheck = x+c-1 in range(xdim)
                                    if wcheck & zcheck & ycheck & xcheck:
                                        neighbors.append(space[w+d-1][z+a-1][y+b-1][x+c-1])       

                    # determining what to append

                    in_test = (w-1 in range(wdim)) & (z-1 in range(zdim)) & (y-1 in range(ydim)) & (x-1 in range(xdim))
                    if in_test:
                        cell = space[w-1][z-1][y-1][x-1] == "#"
                        neig = neighbors.count("#")
                        if cell & ((neig == 2) | (neig == 3)):        # active & 2|3
                            newx_to_append = '#'
                        elif cell & ~((neig == 2) | (neig == 3)):     # active & ~2|3
                            newx_to_append = '.'
                        elif ~cell & (neig == 3):                     # inactive & 3
                            newx_to_append = '#'
                        elif ~cell & ~(neig == 3):                     # inactive & ~3
                            newx_to_append = '.'
                        else:
                            assert 0>0

                    # if we are outside old grid, starts as inactive
                    else:
                        if neighbors.count('#') == 3:
                            newx_to_append = '#'
                        else:
                            newx_to_append = '.'

                    if newx_to_append == "#":
                        cnt +=1

                    newx.append(newx_to_append)
                newy.append(newx)
            newz.append(newy)
        neww.append(newz)
    print(cnt)
    return(neww)

for i in range(6):
    newgrid = play(dat)
    dat = newgrid
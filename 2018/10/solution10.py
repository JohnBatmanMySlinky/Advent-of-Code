import re
import numpy as np
import matplotlib.pyplot as plt
with open("input.txt") as f:
    data = [list(map(int,re.findall(r'-?\d+', x))) for x in f.readlines()]


def plot_p1(data, N):
    dumb = []
    for n in range(N):
        # find bbox
        bbox = [[9999999, 9999999],[-9999999, -9999999]]
        for i, (x,y,vx,vy) in enumerate(data):   
            tmp = [
                [min(bbox[0][0], x+n*vx), min(bbox[0][1], y+n*vy)],
                [max(bbox[1][0], x+n*vx), max(bbox[1][1], y+n*vy)]
            ]
            bbox = tmp
        dumb.append(
            abs(bbox[1][0]-bbox[0][0])**2+abs(bbox[1][1]+bbox[0][1])**2
        )

    plt.plot(range(N),dumb)
    plt.show()

    minimum_val = 999999999999
    minimum_index = 0
    for i,each in enumerate(dumb):
        if each < minimum_val:
            minimum_val = each
            minimum_index = i
    print(f"FUCK: {np.argmin(dumb)}")
    return minimum_index

def p1(data, start, stop):
    for n in range(start, stop):
        # find bbox
        bbox = [[9999999, 9999999],[-9999999, -9999999]]
        for i, (x,y,vx,vy) in enumerate(data):   
            bbox = [
                [min(bbox[0][0], x+n*vx), min(bbox[0][1], y+n*vy)],
                [max(bbox[1][0], x+n*vx), max(bbox[1][1], y+n*vy)]
            ]

        print(f"{n}: ({bbox[0][0]},{bbox[0][1]})x({bbox[1][0]},{bbox[1][1]})--> {abs(bbox[1][0]-bbox[0][0])**2+abs(bbox[1][1]+bbox[0][1])**2} --> ({bbox[1][1]-bbox[0][1]}, {bbox[1][0]-bbox[0][0]})")
        input()
        
        # use max to make board
        board = [["." for _ in range(bbox[1][1]-bbox[0][1]+5)] for _ in range(bbox[1][0]-bbox[0][0]+5)]
        
        # fill board
        for i, (x,y,vx,vy) in enumerate(data):
            board[x+n*vx - bbox[0][0]][y+n*vy - bbox[0][1]] = "#"
        
        print(board)
        input()
        
minidx = plot_p1(data,20000)
print(minidx)
p1(data,minidx-5,minidx+5)



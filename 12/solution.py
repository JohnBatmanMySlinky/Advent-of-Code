import sys
from math import sin, cos, radians

dat = [[x.strip('\n')[0], int(x.strip('\n')[1:])] for x in sys.stdin]

X,Y = 90,0
x,y = 0,0

def COS(N):
    return(round(cos(radians(N)),0))

def SIN(N):
    return(round(sin(radians(N)),0))

for arg in dat:
    # forward is a function of the direction you are facing
    if arg[0] == 'F':
        if (X,Y) == (0,90):
            y += arg[1]
        elif (X,Y) == (0,-90):
            y -= arg[1]
        elif (X,Y) == (90,0):
            x += arg[1]
        elif (X,Y) == (-90,0):
            x -= arg[1]
        else:
            assert 5 == 6

    # mf'n lefts and rights
    if arg[0] == "R":
        tX = X
        tY = Y
        X = COS(arg[1])*tX + SIN(arg[1])*tY
        Y = COS(arg[1])*tY - SIN(arg[1])*tX
    if arg[0] == "L":
        tX = X
        tY = Y
        X = COS(arg[1])*tX - SIN(arg[1])*tY
        Y = COS(arg[1])*tY + SIN(arg[1])*tX

    # cardinal directions
    if arg[0] == 'N':
        y += arg[1]
    if arg[0] == 'S':
        y -= arg[1]
    if arg[0] == 'E':
        x += arg[1]
    if arg[0] == 'W':
        x -= arg[1]
print(abs(x)+abs(y))

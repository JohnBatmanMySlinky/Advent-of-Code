import itertools
from functools import reduce


with open("input.txt") as f:
    data = [[eval(y) for y in x.split('\n')] for x in f.read().split('\n\n')]

def compare(x,y):
    if isinstance(x,int) & isinstance(y,int):
        if x > y:
            return -1
        if x < y:
            return 1
        elif x == y:
            return 0
    elif isinstance(x,list) & isinstance(y,int):
        return compare(x,[y])
    elif isinstance(x,int) & isinstance(y,list):
        return compare([x],y)
    elif isinstance(x,list)&isinstance(y,list):
        z = [compare(xx,yy) for xx,yy in zip(x,y)]
        for zz in z:
            if zz != 0:
                return z
        return compare(len(x), len(y))
    else:
        assert False

from collections.abc import Iterable
def flatten(xs):
    for x in xs:
        if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
            yield from flatten(x)
        else:
            yield x

def p1(data):
    winners = []
    for i,x in enumerate(data):
        deep = compare(*x)
        flat = flatten([deep])
        for f in flat:
            if f == -1:
                break
            elif f == 1:
                winners.append(i+1)
                break
    return sum(winners)


def p2(data):
    A = 1
    B = 1
    for x,y in data:
        z = [x,y]
        for zz in z:
            deep = compare(zz, [[2]])
            flat = flatten([deep])
            for f in flat:
                if f == -1:
                    break
                elif f == 1:
                    A += 1
        for zz in z:
            deep = compare(zz, [[6]])
            flat = flatten([deep])
            for f in flat:
                if f == -1:
                    break
                elif f == 1:
                    B += 1
    return A*(B+1)


print(f"part 1: {p1(data)}")
print(f"part 2: {p2(data)}")
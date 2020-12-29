import sys


dat = [x.split(',') for x in sys.stdin][0]
dat = [int(x) for x in dat]




i = len(dat)    
while i < 2020:
    last_spoken = dat[i-1]
    
    if dat.count(last_spoken) == 1:
        spoken = 0
    elif dat.count(last_spoken) > 1:
        idx = sorted([j for j,k in enumerate(dat) if k == last_spoken], reverse = True)
        a = idx.pop(0)
        b = idx.pop(0)
        spoken = a-b
    else:
        assert 0>0
    
    if i % 1000000 == 0:
        print(i)
    
    dat.append(spoken)
    i += 1
print('part1: ' + str(spoken))
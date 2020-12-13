import sys

dat = [x.strip('\n') for x in sys.stdin]
dat[1] = [int(x) for x in dat[1].split(',') if x != 'x']

log = [0,100]
for bus in dat[1]:
    wait = (1 + int(int(dat[0]) / bus))*bus - int(dat[0])
    if wait < log[1]:
        log[0] = bus
        log[1] = wait
print('part1: ' + str(log[0]*log[1]))
import sys

dat = [int(x.replace('\n', '')) for x in sys.stdin]

N = 25
for i in range(N,len(dat)):
    check = 0
    for a in range(i-N,i):
        for b in range(i-N,i):
            if dat[a]+dat[b] == dat[i]:
                check += 1
    if check == 0:
        broke = dat[i]
        break

# part 1        
print('part1: ' + str(broke))


# part 2
l = 2
stop = False
while (l < len(dat)) & (stop == False):
    for x in range(len(dat)):
        if sum(dat[x:x+l:1]) == broke:
            print('part2: ' + str(min(dat[x:x+l:1])+max(dat[x:x+l:1])))
            stop = True
            break
    l += 1
    







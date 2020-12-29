import sys
from collections import defaultdict

dat = [x.split(',') for x in sys.stdin][0]
dat = [int(x) for x in dat]

spoken_num = defaultdict(list)

# initialize

for i,num in enumerate(dat):
    spoken_num[num].append(i)

last_spoken = dat[-1]    
i = len(dat)
while i < 30000000:
    tmp = spoken_num[last_spoken]
    
    if len(tmp) == 1:
        last_spoken = 0
    elif len(tmp) > 1:
        last_spoken = tmp[-1] - tmp[-2]
    else:
        assert 0>0
    
    if i % 1000000 == 0:
        print(i)
    
    spoken_num[last_spoken].append(i)
    i += 1
print('part2: ' + str(last_spoken))
import sys
import itertools
from collections import defaultdict 

dat = [x.strip('\n').replace('mask = ','').replace('mem[','').replace(']','').split(' = ') for x in sys.stdin]  
mem = defaultdict(int)

def apply_mask2(mask, d):
    b = str(bin(d).replace("0b","")).rjust(36, '0')
    assert len(mask) == 36
    
    new_b = ''
    for i, x in enumerate(mask):
        if x == "0":
            new_b = new_b + b[i]
        if x == "1":
            new_b = new_b + "1"
        if x == "X":
            new_b = new_b + "X"
    
    new_b = [z for z in new_b]
    expanded_new_b = []
    Xs = new_b.count("X")
    for c in [list(x) for x in itertools.product([0,1], repeat = Xs)]:
        tmp_b = new_b[:]
        for i,y in enumerate(tmp_b):
            if y == "X":
                tmp_b[i] = str(c.pop(0))
        expanded_new_b.append(int(''.join(tmp_b),2))
    return(expanded_new_b)

# part 2
for each in dat:
    if len(each) == 1:
        mask = each[0]
        continue
    else:
        idx = int(each[0])
        val = int(each[1])
    
    # PORSED
    for each in apply_mask2(mask, idx):
        mem[each] = val
    
answer = 0
for k,v in mem.items():
    answer += v
print('part2: ' + str(answer))

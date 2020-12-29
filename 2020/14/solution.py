import sys
from collections import defaultdict 

dat = [x.strip('\n').replace('mask = ','').replace('mem[','').replace(']','').split(' = ') for x in sys.stdin]  
mem = defaultdict(int)

def apply_mask(mask, d):
    b = str(bin(d).replace("0b","")).rjust(36, '0')
    assert len(mask) == 36
    
    new_b = ''
    for i, x in enumerate(mask):
        if x == "X":
            new_b = new_b + b[i]
        else:
            new_b = new_b + x
    return(int(new_b,2))

# part 1
for each in dat:
    if len(each) == 1:
        mask = each[0]
        continue
    else:
        idx = int(each[0])
        val = int(each[1])
    
    # PORSED
    mem[idx] = apply_mask(mask, val)
    
answer = 0    
for k,v in mem.items():
    answer += v
print('part1: ' + str(answer))

with open(r"input.txt","r") as f:
    raw = [int(x) for x in f.readlines()[0]]
    
from array import array
from copy import deepcopy
    
   
def FFT(signal, phases, base = [0, 1, 0, -1]):
    to_process = signal.copy()
    for z in range(phases):
        out = array('b', [])
        for i in range(1,len(to_process)+1):
            x = 1
            work = 0
            while True:
                start = ((i*2)*(x-1))+i-1
                end = min(start + i,len(to_process))
                if (x+1) % 2 == 0:
                    mult = 1
                else:
                    mult = -1
                work += mult*sum(to_process[start:end])
                
                if end == len(to_process):
                    break
                    
                x += 1
            out.append(abs(work) % 10)
        to_process = deepcopy(out)
    return to_process

print('part1: ' + ''.join([str(x) for x in FFT(raw,100)[:8]]))


# thanks excel. 
# now it is obvious that [0,1,0,-1]*x where x > len(signal) / 2 then it's justa sum of signal[x:]
# also offset carries through so the raw signal can be offset
# this is still slow as shit so instead of sum(to_process[i:]) % 10 I can work in reverse
offset = int(''.join(map(str, raw[:7])))
new = raw * 10_000

assert offset > len(new)/2

new = new[offset:]

def FFT2(signal, phases):
    to_process = signal.copy()
    for z in range(phases):
        full = sum(to_process)
        out = []
        for i in range(len(to_process)):
            out += [((full % 10) + 10) % 10]
            full -= to_process[i]
        to_process = deepcopy(out)
    return to_process

print('this takes a minutes or three')
print("part2: " + "".join(map(str,FFT2(new, 100)[:8])))

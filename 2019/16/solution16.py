with open(r"input.txt","r") as f:
    raw = [int(x) for x in f.readlines()[0]]
    

def FFT(signal, phases, base = [0, 1, 0, -1]):
    to_process = signal.copy()
    for _ in range(phases):
        out = []
        for i in range(len(to_process)):
            right = [x for x in base for y in range(i+1)]
            right = right*(len(signal) // len(right) + 1)
            right = right[1:]
            prodsum = sum([x*y for x,y in zip(to_process, right)])
            keep = int(str(abs(prodsum))[-1])
            out.append(keep)
        to_process = out
    return to_process
            
print('part1: ' + ''.join([str(x) for x in FFT(raw, 100)[:8]]))
with open('input.txt') as f:
    dat = [int(x) for x in f.readlines()[0].split(',')]

from collections import defaultdict

# start from mode
def mode(dat):
    answer = defaultdict(int)
    for x in dat:
        answer[x] += 1

    out = []
    for k,v in answer.items():
        if v == max(answer.values()):
            out.append(k)
    
    return out


def search1(dat,e=0):
    checked = set()
    modes = mode(dat)
    search_space = list(set([max(x+y,0) for x in modes for y in range(-e,e+1)]))

    results = []
    for x in search_space:
        y = sum([abs(i-x) for i in dat])
        results.append([y,x])


    return sorted(results)[0][0]

def search2(dat,e=0):
    checked = set()
    modes = mode(dat)
    search_space = list(set([max(x+y,0) for x in modes for y in range(-e,e+1)]))

    results = []
    for x in search_space:
        y = sum([sum(range(abs(i-x)+1)) for i in dat])
        results.append([y,x])


    return sorted(results)[0][0]

        
# 500 is totaly arbitrary lol
print(search1(dat,500))
print(search2(dat,500))
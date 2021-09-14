with open(r"input.txt","r") as f:
    formula = {}
    raw = [x.strip().split(" => ") for x in f.readlines()]
    for each in raw:
        x,y = each.pop(-1).split(' ')
        new = {}
        iter = each[0].split(', ')
        while iter:
            w, z = iter.pop(-1).split(' ')
            new[z] = int(w)
        formula[y] = [int(x), new]


from collections import defaultdict

def calc_ore(N):
    need = defaultdict(int, {'FUEL': N})
    xs = defaultdict(int)

    # run till you only have ore left
    while list(need.keys()) != ['ORE']:
        curr = [x for x in need.keys() if x != 'ORE'][0]     
        
        # taking from xs
        if xs[curr] > 0:
            need[curr] -= xs[curr]
            del xs[curr]
        
            if need[curr] == 0:
                del need[curr]

        # how many to make
        mult = (need[curr] - 0.5) // formula[curr][0] + 1

        # adding in xs
        xs[curr] += mult * formula[curr][0] - need[curr]

        # adding sub ingredients
        for each in list(formula[curr][1].keys()):
            need[each] += mult * formula[curr][1][each]

        del need[curr]

    return int(need['ORE'])


print("part1: {}".format(calc_ore(1)))

def search(X, fxn, high, low):
    midpoint = (high + low) // 2
    FUEL = fxn(midpoint)
    kill_N = 5
    kill = [0]*kill_N
    
    while FUEL != X:
#         print(X)        
#         print(midpoint)
#         print(FUEL)
#         print(kill)
#         input()
        
        if FUEL < X:
            low = midpoint
            midpoint = (high+midpoint) // 2
            
        else:
            high = midpoint
            midpoint = (low+midpoint) // 2
    
        FUEL = fxn(midpoint)
        
        kill.append(FUEL)
        kill.pop(0)      
        if len(kill) >= kill_N:
            if all([kill[x] == kill[x+1] for x in range(kill_N-1)]):
                break
            
    
    return midpoint


print("part2: {}".format(search(
    1000000000000, 
    calc_ore, 
    1000000000000*1000,
    0,
)))


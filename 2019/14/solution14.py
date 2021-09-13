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

print(formula)

def calc_ore(ingred, N):
    need = defaultdict(int, {'FUEL': N})
    xs = defaultdict(int)
    ore = 0

    # run till you get primary ingredients
    while list(need.keys()) != ['ORE']:
        curr = [x for x in need.keys() if x != 'ORE'][0]

        # taking from xs
        if xs[curr] - need[curr] > 0:
             need[curr] -= xs[curr]
             del xs[curr]
        elif xs[curr] == need[curr]:
            need[curr] = 0
            del xs[curr]

        mult = (need[curr] - 0.5) // ingred[curr][0] + 1

        # adding in xs
        xs[curr] += mult * ingred[curr][0] - need[curr]

        print(need)
        print(xs)
        print(curr)
        input()

        for each in list(ingred[curr][1].keys()):
            need[each] += mult * ingred[curr][1][each]

        del need[curr]

    return need['ORE']


print(calc_ore(formula, 1))


import re
from copy import deepcopy

with open("input_sample.txt") as f:
    dat = [x.strip()[:-1].replace(":", ".").strip().split(".") for x in f.readlines()]
    costs = []
    for blueprint in dat:
        tmp = []
        for each in blueprint:
            tmp.append(list(map(int,re.findall(r'\d+', each))))
        costs.append(tmp[1:])

robots = [[1,0,0,0]]
ingredients = [[0,0,0,0]]

def build(ingredients, robots, costs):
    new_robots = []
    new_ingredients = []
    for i, ingredient in enumerate(ingredients):
        # build nothing
        new_robots.append([i,0,0,0,0])
        new_ingredients.append([0,0,0,0])

        
        # build geode
        if (ingredient[0] >= costs[3][0])&(ingredient[2] >= costs[3][1]):
            new_robots.append([i,0,0,0,1])
            new_ingredients.append([-costs[3][0],0,-costs[3][1],0])
            # OPTIMIZATION: if you can build a geode, do it
            continue

        # build obsidian
        if (ingredient[0] >= costs[2][0])&(ingredient[1] >= costs[2][1]):
            new_robots.append([i,0,0,1,0])
            new_ingredients.append([-costs[2][0],-costs[2][1],0,0])
            # OPTIMIZATION: if you can build an obsidian do it (unless you can build a geode)
            continue

        # OPTIMIZATION: dont build more than 6 ore robots
        # build ore
        if (ingredient[0] >= costs[0][0])&(robots[i][0]<=14):
            new_robots.append([i,1,0,0,0])
            new_ingredients.append([-costs[0][0],0,0,0])

        # OPTIMIZATION: dont build more than 6 clay robots
        # build clay
        if (ingredient[0] >= costs[1][0])&(robots[i][1]<=14):
            new_robots.append([i,0,1,0,0])
            new_ingredients.append([-costs[1][0],0,0,0])

    return new_robots, new_ingredients

def p1(ROBOTS, INGREDIENTS, costs, minutes):
    results = dict()
    for c, cost in enumerate(costs):
        robots = deepcopy(ROBOTS)
        ingredients = deepcopy(INGREDIENTS)
        for m in range(minutes):
            # see what is buildable
            new_robots, new_ingredients = build(ingredients, robots, cost)

            # build given existing robots
            for i in range(len(ingredients)):
                ingredients[i] = [a+b for a,b in zip(ingredients[i], robots[i])]
                
            # expand universes
            for i in range(len(new_ingredients)):
                old_i = new_robots[i].pop(0)
                new_ingredients[i] = tuple([aa+bb for aa,bb in zip(new_ingredients[i],ingredients[old_i])])
                new_robots[i] = tuple([aa+bb for aa,bb in zip(new_robots[i],robots[old_i])])
            ingredients = new_ingredients[:]
            robots = new_robots[:]

            # if you have too much ore, PRUNE
            tmp = list(map(list, zip(*[(I,R) for I,R in zip(ingredients, robots) if I[0]<16])))
            ingredients = tmp[0]
            robots = tmp[1]

            # print(f"ingredients: {ingredients}")
            # print(f"robots     : {robots}")
            # print(f"minute: {m+1}")
            # print(f"the universe is {len(ingredients):,} long")
            # print(f"most obsidian: {max(z[2] for z in ingredients)}")
            # print(f"most geodes: {max(z[3] for z in ingredients)}")
            # input()
        print(f"done with blueprint: {c+1}")
        results[c+1] = max(z[3] for z in ingredients)
    return sum(k*v for k,v in results.items())
# print(f"part 1: {p1(robots, ingredients, costs, 24)}")
print(f"part 1: {p1(robots, ingredients, costs, 32)}")
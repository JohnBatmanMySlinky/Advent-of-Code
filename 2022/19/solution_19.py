import re
from copy import deepcopy

with open("input_sample.txt") as f:
    dat = [x.strip()[:-1].replace(":", ".").strip().split(".") for x in f.readlines()]
    costs = []
    for blueprint in dat:
        print(blueprint)
        tmp = []
        for each in blueprint:
            tmp.append(list(map(int,re.findall(r'\d+', each))))
        costs.append(tmp)

robots = {
    "ore": 1,
    "clay": 0,
    "obsidian": 0,
    "geode": 0,
}
ingredients = {
    "ore": 0,
    "clay": 0,
    "obsidian": 0,
    "geode": 0
}

universe = [(ingredients, robots)]

def spawn_universes(universe, cost):
    universe_adj = []
    new_universe = []
    for I,R in universe:
        # copy over unchanged universe
        new_universe.append((I,R))
        universe_adj.append([{}, {}])

        # cost
        # = [[blue print #], [ore], [clay], [obsidian, obsidian], [geode, geode]]

        # what if we instead dont build shitty universes

        # build an ore robot
        if (I["ore"] >= cost[1][0])&(R["ore"] < 6):
            new_universe.append(deepcopy((I,R)))
            universe_adj.append([{"ore": -cost[1][0]}, {"ore": 1}])
        # build a clay robot
        if (I["ore"] >= cost[2][0])&(R["clay"]<6):
            new_universe.append(deepcopy((I,R)))
            universe_adj.append([{"ore": -cost[2][0]}, {"clay": 1}])
        # build a obsidian robot
        if (I["ore"] >= cost[3][0])&(I["clay"] >= cost[3][1]):
            new_universe.append(deepcopy((I,R)))
            universe_adj.append([{"ore": -cost[3][0], "clay": -cost[3][1]}, {"obsidian": 1}])
        # build a geode robot
        if (I["ore"] >= cost[4][0])&(I["obsidian"] >= cost[4][1]):
            new_universe.append(deepcopy((I,R)))
            universe_adj.append([{"ore": -cost[4][0], "obsidian": -cost[4][1]}, {"geode": 1}])
        
    return new_universe, universe_adj

def p1(UNIVERSE, costs):
    results = {}
    for cost in costs:
        universe = UNIVERSE[:]
        for i in range(1,25):
            print(f"blueprint: {cost[0][0]}, minute: {i}, number of universes being simulated: {len(universe):,}")      
            # print(f"len of universe: {len(universe)}")
            # print(f"Most clay robots in any universe: {max([R['clay'] for I,R in universe])}")
            # split universe on decision to spend & build or not
            universe, universe_adj = spawn_universes(universe, cost)

            # every robot that exists advances collection count
            for I, R in universe:
                for robot_type, robot_num in R.items():
                    I[robot_type] += robot_num

            # now that building is done            
            # merge universe and universe adj
            for (I, R),(Iadj, Radj) in zip(universe, universe_adj):
                for k in I.keys():
                    I[k] += Iadj.get(k,0)
                for k in R.keys():
                    R[k] += Radj.get(k,0)

            
            # now lets make up some hueristic to prune shitty paths
            # kill resource hoarders
            if max([max(I.values()) for I,R in universe]) > 16:
                less_shitty_universe = [(I,R) for I,R in universe if max(I.values())<=16]
                universe = less_shitty_universe[:]
            
            # if you have more than 5 ore robots, that's shitty
            # less_shitty_universe = [(I,R) for I,R in universe if R["ore"]<5]
            # universe = less_shitty_universe[:]

            # only keep a set of universes dummy
            less_shitty_universe = []
            for I,R in universe:
                if (I,R) not in less_shitty_universe:
                    less_shitty_universe.append((I,R))
            universe = less_shitty_universe[:]

        results[cost[0][0]] = max([I['geode'] for I,R in universe])
        print(results)
    return sum([k*v for k,v in results.items()])

print(f"part 1: {p1(universe, costs)}")
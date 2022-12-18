with open("input.txt") as f:
    data = [list(x.strip()) for x in f.readlines()][0]

def make_cave(X,Y):
    return [['.' for x in range(X)] for y in range(Y)]

def find_floor(cave, rock_dict):
    if len(rock_dict["resting"]) > 0:
        return min(z[1] for z in rock_dict["resting"])-4
    else:
        return len(cave)-4
    
def spawn_rocks(cave, rock_dict, r):
    floor = find_floor(cave, rock_dict)
    if r == 0:
        cave[floor][2] = '@'
        cave[floor][3] = '@'
        cave[floor][4] = '@'
        cave[floor][5] = '@'
        rock_dict["falling"] = {(2,floor), (3,floor), (4,floor), (5,floor)}
    elif r == 1:
        cave[floor  ][3] = '@'
        cave[floor-1][2] = '@'
        cave[floor-1][3] = '@'
        cave[floor-1][4] = '@'
        cave[floor-2][3] = '@'
        rock_dict["falling"] = {(3,floor), (2,floor-1), (3,floor-1), (4,floor-1), (3, floor-2)}
    elif r == 2:
        cave[floor  ][2] = '@'
        cave[floor  ][3] = '@'
        cave[floor  ][4] = '@'
        cave[floor-1][4] = '@'
        cave[floor-2][4] = '@'
        rock_dict["falling"] = {(2,floor), (3,floor), (4,floor), (4,floor-1), (4,floor-2)}
    elif r == 3:
        cave[floor  ][2] = '@'
        cave[floor-1][2] = '@'
        cave[floor-2][2] = '@'
        cave[floor-3][2] = '@'
        rock_dict["falling"] = {(2,floor), (2,floor-1), (2,floor-2), (2,floor-3)}
    elif r == 4:
        cave[floor  ][2] = '@'
        cave[floor  ][3] = '@'
        cave[floor-1][2] = '@'
        cave[floor-1][3] = '@'
        rock_dict["falling"] = {(2,floor), (3,floor), (2,floor-1), (3,floor-1)}
    else:
        assert False
    return cave, rock_dict

def push_rock(cave, rock_dict, gas):
    if gas == ">":
        newset = set()
        for x,y in rock_dict["falling"]:
            newset.add((x+1,y))
        rightmost = max([z[0] for z in rock_dict["falling"]])        
        if (rightmost+1 < len(cave[0])) & (len(newset & rock_dict["resting"]) == 0):
            # erase old cave
            for x,y in rock_dict["falling"]:
                cave[y][x] = '.'
            for x,y in newset:
                cave[y][x] = "@"
            rock_dict["falling"] = newset
    elif gas == "<":
        newset = set()
        for x,y in rock_dict["falling"]:
            newset.add((x-1,y))
        leftmost = min([z[0] for z in rock_dict["falling"]])
        # CHECK INTERSECTION WITH RESTING
        if (leftmost-1 >= 0)  & (len(newset & rock_dict["resting"])== 0 ):
            # erase old cave
            for x,y in rock_dict["falling"]:
                cave[y][x] = '.'
            for x,y in newset:
                cave[y][x] = "@"
            rock_dict["falling"] = newset
    else:
        assert False    
    return cave, rock_dict

def fall_rock(cave, rock_dict):
    falling = True
    if len(rock_dict["resting"]) == 0:
        bottom_most = max(z[1] for z in rock_dict["falling"])
        if bottom_most + 1 == len(cave):
            falling = False
            rock_dict = {"falling": set(), "resting": rock_dict["falling"]}
        elif bottom_most + 1 < len(cave):
            for x,y in rock_dict["falling"]:
                cave[y][x] = '.'
            newset = set()
            for x,y in rock_dict["falling"]:
                cave[y+1][x] = "@"
                newset.add((x,y+1))
            falling = True
            rock_dict["falling"] = newset
        else:
            assert False
    else:
        newset = set()
        for x,y in rock_dict["falling"]:
            newset.add((x,y+1))
        if len(newset & rock_dict["resting"])>0:
            falling = False
            rock_dict = {"falling": set(), "resting": rock_dict["resting"] | rock_dict["falling"]}
        else:
            for x,y in rock_dict["falling"]:
                cave[y][x] = '.'
            for x,y in newset:
                cave[y][x] = "@"
            rock_dict["falling"] = newset

    return cave, rock_dict, falling

def p1(gas_stream, rocks):
    cave = make_cave(7,4_000)
    rock_dict = {"falling": set(), "resting": set()}
    i = 0
    for r in range(rocks):
        # print(r)
        cave, rock_dict = spawn_rocks(cave, rock_dict, r%5)
        falling = True
        # print(cave, rock_dict)
        # input()
        # print()
        while falling:
            gas = gas_stream[i]
            # really should have one function here for push and fall and pass in tuples of directions to be moved
            # too late
            cave, rock_dict = push_rock(cave, rock_dict, gas)
            # print(gas)
            # print(cave,rock_dict)
            # input()
            cave, rock_dict, falling = fall_rock(cave, rock_dict)
            # print(cave, rock_dict)
            # input()
            i += 1    
    return len(cave) - min(z[1] for z in rock_dict["resting"])

def find_pattern(log):
    print("looking 4 a pattern")
    window = 60
    for x in range(len(log)):
        for y in range(x+1, len(log)):
            a = [z[:2] for z in log[x:(x+window)]]
            b = [z[:2] for z in log[y:(y+window)]]
            # print(a,b)
            # input()
            if a == b:
                return x,y

def p2(gas_stream, rocks):
    cave = make_cave(7,15_000)
    rock_dict = {"falling": set(), "resting": set()}
    i = 0
    log = []
    for r in range(rocks):
        # if (r % 1000 == 0) & (r > 0):
            # print(r)
        cave, rock_dict = spawn_rocks(cave, rock_dict, r%5)
        falling = True
        gaslog = ""
        while falling:
            gas = gas_stream[i]
            gaslog += gas
            cave, rock_dict = push_rock(cave, rock_dict, gas)
            cave, rock_dict, falling = fall_rock(cave, rock_dict)
            i += 1    

        log.append([r%5, gaslog, len(cave) - min(z[1] for z in rock_dict["resting"]), r])
        # print([x[:2] for x in log])
        # input()

    cycle_base, cycle_length = find_pattern(log)
    cycle_length -= cycle_base
    print(f"cycle base: {cycle_base:,}, cycle length: {cycle_length}")

    base_height = log[cycle_base][2]
    cycle_height = log[cycle_length][2]
    print(f"base height: {base_height:,}, cycle height: {cycle_height}")

    for i in range(6):
        print(log[cycle_base+cycle_length* i])
        print(base_height + cycle_height * i - i)
        print()

    AH = 1_000_000_000_000

    cycles = (AH - cycle_base)//cycle_length
    answer = base_height + cycle_height * cycles - cycles
    cycles_left = AH - cycles * cycle_length + cycle_base
    answer += log[cycle_base+cycle_length+cycles_left][2]-log[cycle_base+cycle_length][2] - base_height
    return answer

# print(f"part 1: {p1(data)}")
print(f"part1: {p1(data*100, 2_022)}")
print(f"part2: {p2(data*100, 10_000)}")
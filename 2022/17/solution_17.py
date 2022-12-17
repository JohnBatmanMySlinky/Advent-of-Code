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

# print(f"part 1: {p1(data)}")
print(f"{p1(data*100, 2022)}")
with open(r"input.txt","r") as f:
    start_fish = [int(x) for x in f.readlines()[0].strip().split(',')]

from collections import deque

transform = {
    0:6,
    1:0,
    2:1,
    3:2,
    4:3,
    5:4,
    6:5,
    7:6,
    8:7,
}


def make_fish(N, old_fish):
    for i in range(N):
        new_fish = deque([])
        for fish in old_fish:
            new_fish.append(transform[fish])
            if fish == 0:
                new_fish.append(8)

        old_fish = new_fish

    return len(new_fish)



def make_fish_p2(N, old_fish):
    school = {k:0 for k in range(9)}
    
    for fish in old_fish:
        school[fish] += 1

    for _ in range(N):
        ugh = school[0]
        for x in [0,1,2,3,4,5,6,7]:
            school[x] = school[x+1]
        school[6] += ugh
        school[8] = ugh

        # print(school)
        # input()

    return sum(school.values())



print(make_fish(80, start_fish))
print(make_fish_p2(256, start_fish))
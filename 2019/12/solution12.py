with open("input.txt") as f:
    raw = [x.replace("<","").replace(">","").replace("x=","").replace("y=","").replace("z=","").replace("\n","").split(",") for x in f.readlines()]
    moons = []    
    vel = []    
    for moon in raw:
        tmp = []
        tmp_vel = []
        for coord in moon:
            tmp.append(int(coord))
            tmp_vel.append(0)
        moons.append(tmp)
        vel.append(tmp_vel)
        
from copy import deepcopy
import math
            
def simulate_p1(N, moons, vel):
#     print(moons)
#     print(vel)
    
    # simulate
    for n in range(1,N+1):
        moons_new = deepcopy(moons)
        
        # velocity
        # for each moon
        for moon in range(len(moons)):
            # loop through X, Y, Z
            for dim in range(len(moons[0])):
                tmp = 0
                
                for each in range(len(moons)):
                    if moons[each][dim] > moons[moon][dim]:
                        tmp += 1
                    elif moons[each][dim] < moons[moon][dim]:
                        tmp -= 1
                    else:
                        tmp += 0

                vel[moon][dim] += tmp
                moons_new[moon][dim] += vel[moon][dim]
        moons = deepcopy(moons_new)
#     print("===================")
#     print(moons)
#     print(vel)
    
    t_energy = 0
    # calculate total energy
    for i in range(len(moons)):
        k_energy = sum([abs(x) for x in moons[i]])
        p_energy = sum([abs(x) for x in vel[i]])
        t_energy += k_energy * p_energy
    
    return(t_energy)


def simulate_axis(AXIS, moons, vel):
#     print([x[AXIS] for x in moons])
#     print([y[AXIS] for y in vel])

    state_orig = [x[AXIS] for x in moons] + [y[AXIS] for y in vel]
    i = 0
    
    # simulate
    while True:
        moons_new = deepcopy(moons)
        
        # velocity
        # for each moon
        for moon in range(len(moons)):
            dim = AXIS
            tmp = 0

            for each in range(len(moons)):
                if moons[each][dim] > moons[moon][dim]:
                    tmp += 1
                elif moons[each][dim] < moons[moon][dim]:
                    tmp -= 1
                else:
                    tmp += 0

            vel[moon][dim] += tmp
            moons_new[moon][dim] += vel[moon][dim]
        moons = deepcopy(moons_new)
#         print([x[AXIS] for x in moons])
#         print([y[AXIS] for y in vel])
        
        i += 1
        
        state = [x[AXIS] for x in moons] + [y[AXIS] for y in vel]
        if state == state_orig:
            return i
        else:
            pass
            
        assert i < 1_000_000

def least_common_multiple(x, y):
    return (x * y) // math.gcd(x, y)

moons_a = deepcopy(moons)
vel_a = deepcopy(vel)
moons_b = deepcopy(moons)
vel_b = deepcopy(vel)
moons_c = deepcopy(moons)
vel_c = deepcopy(vel)
moons_d = deepcopy(moons)
vel_d = deepcopy(vel)



print("part1: {}".format(simulate_p1(1_000, moons_a, vel_a)))
        

b = simulate_axis(0,moons_b,vel_b)
c = simulate_axis(1,moons_c,vel_c)
d = simulate_axis(2,moons_d,vel_d)

print("part2: {}".format(least_common_multiple(least_common_multiple(b,c),d)))
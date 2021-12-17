with open('input.txt') as f:
    dat = [x for x in f.readlines()][0]

import re
x1 = re.findall("x\=[0-9]+\.\.", dat)[0]
x1 = x1[2:]
x1 = int(x1[:-2])

x2 = re.findall("\.\.[0-9]+,", dat)[0]
x2 = x2[2:]
x2 = int(x2[:-1])

y1 = int(re.findall("-[0-9]+", dat)[0])

y2 = int(re.findall("-[0-9]+", dat)[1])

def check_target(pos, square):
    x,y = pos
    a,b,c,d = square

    if a <= x <= b and c <= y <= d:
        return True
    else:
        return False

def hurl(start,target, vel):
    x,y = start
    j,k = vel
    y_path = [y]

    for i in range(200):
        x += j # increment x
        y += k # increment y
        k -= 1 # gravity

        # slightly more complicated x vel
        if j < 0:
            j += 1
        elif j > 0:
            j -= 1
        elif j == 0:
            pass
        else:
            assert False

        y_path.append(y)

        if check_target((x,y), target):
            return max(y_path)
    return None
        
def p1(target):
    highest = 0
    for a in range(0,100):
        for b in range(0,100):
            result = hurl((0,0), target, (a,b))
            if result is not None:
                if result > highest:
                    highest = result

    return highest

def p2(target, N):
    success = 0
    for a in range(-N,N):
        for b in range(-N,N):
            result = hurl((0,0), target, (a,b))
            if result is not None:
                success += 1
    return success


print(p1((x1, x2, y1, y2)))
print(p2((x1, x2, y1, y2), 500))
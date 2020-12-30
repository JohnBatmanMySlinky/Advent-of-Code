import sys
from collections import deque

dat = [int(x) for x in sys.stdin.read()]

dat = dat + [x for x in range(max(dat)+1,1000001)]
assert len(dat) == len(set(dat))
# 389125467

# building linked list as a dictionary
def make_dict(dat):    
    hand = {}
    for i in range(len(dat)):
        hand[dat[i]] = dat[(i+1)%len(dat)]
    return(hand)

# pick up 3 cups clockwise to current 
def pickup_3_CW(d,pos):
    pickup = deque()
    for _ in range(3):
        pos = d[pos]
        pickup.append(pos)
    return(pickup)

def destination(c, pu):
    dest = current - 1
    if dest == 0:
        dest = len(dat)
    while dest in pickup:
        dest -= 1
        if dest == 0:
            dest = len(dat)
    return(dest)

def insert(hand, curr, d, pu):
    left = pu.popleft()
    right = pu.pop()
    hand[curr] = hand[right]
    hand[right] = hand[d]
    hand[d] = left
    return(hand)

def score(hand):
    answer = []
    cup = 1
    for _ in range(len(hand)-1):
        answer.append(hand[cup])
        cup = hand[cup]
    return(''.join([str(x) for x in answer]))
           

# play
current = dat[0]
hand = make_dict(dat)
for john in range(10000000):   
    if john % 1000000 == 0:
        print(john)
    
    # pick up 3
    pickup = pickup_3_CW(hand, current)
    
    # destination of picked up cups
    dest = destination(current, pickup)
    
    # insert picked up cups back into dictionary
    hand = insert(hand, current, dest, pickup)
    
    # adv current
    current = hand[current]

print('part2: ' + str(hand[1] * hand[hand[1]]))

    


    
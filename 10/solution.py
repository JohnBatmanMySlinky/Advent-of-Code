import sys

dat = sorted([int(x.strip('\n')) for x in sys.stdin])

# part 1
one = 1
three = 1
for i in range(len(dat)-1):
    if dat[i+1]-dat[i] == 1:
        one += 1
    elif dat[i+1]-dat[i] == 3:
        three += 1
    else:
        assert 5 == 6
print('part1: ' + str(one*three))


# oh jeez this part 2 is awful
dat = [0] + dat + [max(dat)+3]
distance = [0]*(len(dat)-1)
answer = [1]*len(distance)
for x in range(len(dat)-1):
    #distance (either 1 or 3)
    distance[x] = dat[x+1]-dat[x]
  
    # count back to see how many consequtive 1's there are
    if x > 0:
        cnt = 0
        for y in range(x-1,-1,-1):
            if distance[y] == 3:
                break
            else:
                cnt += 1
                
        # consequtive 1s less than 2 can't be mutated
        # consequtive 1s more than 3 can only have 3 be mutated
        if cnt >= 2:
            if cnt > 3:
                cnt = 3
            tmp = 0
            for z in range(1,cnt+1):
                # recursively add earlier trees
                tmp += answer[x-z]
            answer[x] = tmp
        else:
                answer[x] = answer[x-1]
print('part2: ' + str(answer[-1]))

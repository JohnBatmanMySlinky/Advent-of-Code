with open(r"input.txt","r") as f:
    dat = [x.strip() for x in f.readlines()]

from operator import lt, gt, le, ge

def part1(dat):
    gamma = ''
    for n in range(len(dat[0])):
        zero = 0
        for x in dat:
            if x[n] == '0':
                zero += 1
        if zero > len(dat)/2:
            gamma += '0'
        else: 
            gamma += '1'
    
    epsilon = ''.join(['0' if y == '1' else '1' for y in gamma])

    return int('0b'+gamma,2) * int('0b'+epsilon,2)

print(part1(dat))

def part2(dat, signs):
    answer = []
    for fxn in signs:
        oxygen = dat.copy()
        bit = 0
        while len(oxygen)>1:
            # count bits
            zero = 0
            for each in oxygen:
                if each[bit] == '0':
                    zero += 1

            # which gets dropped
            if fxn(zero,len(oxygen)-zero):
                mask = '1'
            else:
                mask = '0'

            new_oxygen = []
            for x in range(len(oxygen)):
                if oxygen[x][bit] == mask:
                    new_oxygen.append(oxygen[x])
            oxygen = new_oxygen

            # print(mask)
            # print(oxygen)
            # input()

            bit += 1
        answer.append(oxygen[0])

    return int('0b'+answer[0],2) * int('0b'+answer[1],2)

print(part2(dat, [le, gt]))




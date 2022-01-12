with open('input.txt') as f:
    dat = [x.strip().split(' | ') for x in f.readlines()]
    dat = [[x.split(' '),y.split(' ')] for x,y in dat]


part1_dict = {
    2: 0, # 1
    4: 0, # 4
    3: 0, # 7
    7: 0, # 8
}

def part1(dat):
    for l,r in dat:
        for i in r:
            if len(i) in part1_dict.keys():
                part1_dict[len(i)] += 1
    return sum(part1_dict.values())
print(part1(dat))







def decode(signals):
    mapper = {}

    # get 1,7,4,8 out of the way
    for signal in signals:
        if len(signal) == 2:
            mapper[1] = signal
        elif len(signal) == 4:
            mapper[4] = signal
        elif len(signal) == 3:
            mapper[7] = signal
        elif len(signal) == 7:
            mapper[8] = signal

    # figure out a and c&f
    a = set([x for x in mapper[7]]) - set([x for x in mapper[1]])
    cf = [x for x in mapper[1]]

    # know 6 as it doesn't have c&f of 0,6,9 
    mapper[6] = [x for x in signals if len(x)==6 and not (x.find(cf[0])>-1 and x.find(cf[1])>-1)][0]

    # know 0 as it doesn't have full intersect 2,5,3 (adg)
    len5 = [set(x) for x in signals if len(x)==5]
    adg = ''.join(set.intersection(*len5))
    mapper[0] = [x for x in signals if len(x)==6 and not (x.find(adg[0])>-1 and x.find(adg[1])>-1 and x.find(adg[2])>-1)][0]

    # know 9 as we know 6,0,9
    mapper[9] = [x for x in signals if len(x)==6 and x not in mapper.values()][0]

    # know 3 as it has c&f out of 2,5,3
    mapper[3] = [x for x in signals if len(x)==5 and x.find(cf[0])>-1 and x.find(cf[1])>-1][0]

    # know 2 as it has e out of 2,5
    e = ''.join(set(mapper[8]) - set(mapper[9]))
    mapper[2] = [x for x in signals if len(x)==5 and x not in mapper.values() and x.find(e)>-1][0]

    # five is left over
    mapper[5] = [x for x in signals if x not in mapper.values()][0]

    assert len(set(mapper.values())) == len(mapper.values())

    return mapper


def part2(dat):
    answer = []
    for z,(x,y) in enumerate(dat):
        mapper = decode(x)
        
        # sort values and make them the keys
        new_mapper = {}
        for k,v in mapper.items():
            new_mapper[''.join(sorted(v))] = k

        # translate the message into list of ints
        tmp = []
        for i in y:
            tmp.append(new_mapper[''.join(sorted(i))])
        
        # translate list of ints to number
        answer.append(int(''.join([str(j) for j in tmp])))
    return sum(answer)

print(part2(dat))


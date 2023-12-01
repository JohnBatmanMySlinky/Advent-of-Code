def p1():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    all_num = [str(x) for x in range(1,10)]
    total = 0

    for line in lines:
        current = []
        for each in line:
            if each in all_num:
                current.append(each)
        total += int(current[0]+current[-1])
    return total

def p2():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    all_num = {"one":"1", "two":"2", "three":'3', "four":'4', "five":'5', "six":'6', "seven":'7', "eight":'8', "nine":'9'}
    tmp = {str(x):str(x) for x in range(1,10)}
    all_num.update(tmp)
    total = 0

    for line in lines:
        current = []
        for each in all_num.keys():
            ps = smartfind(line, each)
            for p in ps:
                current.append([p, all_num[each]])
        current = sorted(current, key = lambda x: x[0])
        total += int(current[0][1]+current[-1][1])
    return total

def smartfind(word, target):
    log = []
    startfrom = 0
    search = True
    while search:
        p = word[startfrom:].find(target)
        # print(startfrom, word[startfrom:], p)
        # input()
        if p > -1:
            startfrom += p+1
            log.append(startfrom-1)
        else:
            search = False
    return [x for i,x in enumerate(log)]

answer1 = p1()
print(f"p1: {answer1}")
answer2 = p2()
print(f"p2: {answer2}")
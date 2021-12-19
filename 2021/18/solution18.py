with open('input.txt') as f:
    dat = [eval(x.strip()) for x in f.readlines()]

def parse(number, d):
    for each in number:
        if isinstance(each, list):
            yield from parse(each, d + 1)
        else:
            yield each, d

def explode(number):
    for i,(x,d) in enumerate(number):
        if d==4:
            if i>0: # explode left
                number[i-1] = (number[i-1][0] + x, number[i-1][1])
            if i+2<len(number): # explode right
                number[i+2] = (number[i+1][0] + number[i+2][0], number[i+2][1])
            number[i] = (0,3)
            if i+1<len(number):
                number[i+1] = (-1,-1)
            return [x for x in number if x[0] != -1], True
    return number, False

def split(number):
    for i,(x,d) in enumerate(number):
        if x >= 10:
            # FUCK
            if x//2 == x/2: # FUCK EVEN
                number[i] = (int(x/2),d+1)
                number.insert(i+1, (int(x/2),d+1))
            else: # FUCK ODD
                number[i] = (x//2,d+1)
                number.insert(i+1, (x//2+1,d+1))
            return number, True
    return number, False

def part1(dat):
    code = list(parse(dat[0],0))
    for each in dat[1:]:

        new = list(parse(each,0))

        code += new
        code = [(x,y+1) for x,y in code]

        while True:
            print(code, sum([x+y for x,y in code]))
            code, result = explode(code)
            if result == True: continue

            code, result = split(code)
            if result == True: continue

            break

    return code

def magnitude(code):
    print(code)
    maxdepth = max([y for x,y in code])
    print("max depth: {}".format(maxdepth))
    for d in reversed(range(1,maxdepth+1)):
        for i, (x,y) in enumerate(code):
            if y == d:
                code[i] = (x*3+code[i+1][0]*2, y-1)
                code[i+1] = (-1, -1)
        code = [(x,y) for x,y in code if x != -1]
    return code[0][0]


# print(part1(dat))

print(magnitude(list(parse(dat,0))))
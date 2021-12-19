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
        print(code)
        input()

        while max([y for x,y in code]) >= 4:
            code, result = explode(code)
            if not result:
                code, result = split(code)

    while True:
        print(code)
        input()
        code, result = explode(code)
        if not result:
            code, result = split(code)

# print(explode(list(parse(dat,0))))
print(part1(dat))
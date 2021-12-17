from functools import reduce
with open('input.txt') as f:
    dat = [[y for y in x.strip()] for x in f.readlines()]

fuck = {
    '0':'0000',
    '1':'0001',
    '2':'0010',
    '3':'0011',
    '4':'0100',
    '5':'0101',
    '6':'0110',
    '7':'0111',
    '8':'1000',
    '9':'1001',
    'A':'1010',
    'B':'1011',
    'C':'1100',
    'D':'1101',
    'E':'1110',
    'F':'1111'
}

def hex_to_int(h):
    return list(''.join([fuck[x] for x in h]))

vsum = 0
def p1(code):
    global vsum
    version = ''.join(code[:3]) 
    vsum += int(hex(int(version,2))[2:])
    id = ''.join(code[3:6])
    idhex = hex(int(id,2))[2:]

    code = code[6:]
    if idhex == '4':
        literal = ''
        while True:
            ind = code.pop(0)
            literal += ''.join([code.pop(0) for _ in range(4)])
            if ind == '0':
                break
        return code, int(literal,2)
    else:
        typeid = code.pop(0)
        answer = []
        if typeid == '0':
            length = int(''.join([code.pop(0) for _ in range(15)]),2)
            to_be_parsed = code[:length]
            while to_be_parsed:
                to_be_parsed, literal = p1(to_be_parsed)
                answer.append(literal)
            code = code[length:]
        else:
            length = int(''.join([code.pop(0) for _ in range(11)]),2)
            for _ in range(length):
                code, literal = p1(code)
                answer.append(literal)

        if idhex == '0':
            return code, sum(answer)
        elif idhex == '1':
            return code, reduce((lambda x, y: x * y), answer)
        elif idhex == '2':
            return code, min(answer)
        elif idhex == '3':
            return code, max(answer)
        elif idhex == '5':
            return code, 1 if answer[0]>answer[1] else 0
        elif idhex == '6':
            return code, 1 if answer[0]<answer[1] else 0
        elif idhex == '7':
            return code, 1 if answer[0]==answer[1] else 0
    return code, answer


print("part 1: {}".format(str(p1(hex_to_int(dat[0]))[1])))
print("part 2: {}".format(str(vsum)))
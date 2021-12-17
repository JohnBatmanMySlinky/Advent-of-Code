with open('input.txt') as f:
    dat = [[y for y in x.strip()] for x in f.readlines()]

def hex_to_int(h):
    return list(bin(int(''.join(h),16))[2:])
    
def parse_subpacket(code):
    literal = ''
    while True:
        ind = code.pop(0)
        val = ''.join([code.pop(0) for _ in range(4)])
        literal += val
        if ind == '0':
            break
    return int(literal,2), code

vsum = 0
def p1(code):
    global vsum
    version = ''.join([code.pop(0) for _ in range(3)]) 
    vsum += int(hex(int(version,2))[2:])
    id = ''.join([code.pop(0) for _ in range(3)])
    idhex = hex(int(id,2))[2:]

    if idhex == '4':
        literal, _ = parse_subpacket(code)
    else:
        typeid = code.pop(0)
        if typeid == '0':
            length = int(''.join([code.pop(0) for _ in range(15)]),2)
            to_be_parsed = code[:length]
            while to_be_parsed:
                p1(to_be_parsed)
        if typeid == '1':
            length = int(''.join([code.pop(0) for _ in range(11)]),2)
            for _ in range(length):
                p1(code)

    return vsum

print(p1(hex_to_int(dat[0])))
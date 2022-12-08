with open("input.txt") as f:
    data = [list(map(int, list(x.strip()))) for x in f.readlines()]

def perimeter(data):
    return len(data) * 2 + len(data[0]) * 2 - 4

def p1(data):
    new = [[0 for x in range(len(data[0]))] for y in range(len(data))]
    for col in range(1,len(data)-1):
        for row in range(1,len(data[0])-1):

            tmp = []
            for y in range(0,col):
                tmp.append(data[y][row])
            if max(tmp) < data[col][row]:
                new[col][row] += 1

            tmp = []
            for y in range(col+1,len(data)):
                tmp.append(data[y][row])
            if max(tmp) < data[col][row]:
                new[col][row] += 1

            if max(data[col][0:row]) < data[col][row]:
                new[col][row] += 1
            if max(data[col][(row+1):len(data[0])]) < data[col][row]:
                new[col][row] += 1
    visible = 0
    for col in new:
        for i in col:
            if i > 0:
                visible += 1
    return visible + perimeter(data)


def p2(data):
    new = [[0 for x in range(len(data[0]))] for y in range(len(data))]
    for col in range(1,len(data)-1):
        for row in range(1,len(data[0])-1):

            UP = 0
            for y in reversed(range(0,col)):
                if data[y][row] < data[col][row]:
                    UP += 1
                else:
                    UP += 1
                    break

            DOWN = 0
            for y in range(col+1,len(data)):
                if data[y][row] < data[col][row]:
                    DOWN += 1
                else:
                    DOWN += 1
                    break

            LEFT = 0
            for x in reversed(range(0,row)):
                if data[col][x] < data[col][row]:
                    LEFT += 1
                else:
                    LEFT += 1
                    break

            RIGHT = 0
            for x in range(row+1,len(data[0])):
                if data[col][x] < data[col][row]:
                    RIGHT += 1
                else:
                    RIGHT += 1
                    break

            new[col][row] = UP * DOWN * LEFT * RIGHT
    return max([max([x for x in y])for y in new])
    




print(f"part 1: {p1(data)}")
print(f"part 2: {p2(data)}")
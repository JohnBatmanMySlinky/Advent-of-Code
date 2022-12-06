with open("input.txt") as f:
    data = [x for x in f.readlines()[0]]

def p12(data,N):
    for i in range(len(data)-N):
        if len(set(data[i:(i+N)])) == N:
            return i+N


print(f"part1: {p12(data, 4)}")
print(f"part1: {p12(data, 14)}")
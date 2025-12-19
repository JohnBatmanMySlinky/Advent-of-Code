with open("input.txt", "r") as f:
    data = [x.strip() for x in f.readlines()]

def p1(data):
    tot = 0
    for line in data:
        maxx = 0
        for a in range(len(line)):
            for b in range(a+1, len(line)):
                maybe = int(line[a]+line[b])
                if maybe > maxx:
                    maxx = maybe
        tot += maxx
    return tot

answer = p1(data)
print(f"part 1: {answer}")
with open("input.txt", "r") as f:
    data = [list(map(int,x.strip().replace('-',',').split(','))) for x in f.readlines()]

def p1(data):
    winner = 0
    for a,b,x,y in data:
        winner += ((a >= x)&(b <= y)) | ((x >= a)&(y <= b))
    return winner

def p2(data):
    winner = 0
    for a,b,x,y in data:
        winner += len(set(range(a,b+1)) & set(range(x,y+1))) > 0
    return winner

print(f"part 1: {p1(data)}")
print(f"part 2: {p2(data)}")
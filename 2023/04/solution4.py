def p1():
    with open("input.txt","r") as f:
        data = [x.split(": ")[1].split(" | ") for x in f.readlines()]
    data = [[list(map(int,x.replace("  "," ").strip().split(" "))),list(map(int,y.replace("  "," ").strip().split(" ")))] for x,y in data]
    
    answer = 0
    for left, right in data:
        score = 0
        for each in left:
            if each in right:
                score += 1
        if score > 0 :
            answer += 2 ** (score-1)

    return answer


def p2():
    with open("input.txt","r") as f:
        data = [x.split(": ")[1].split(" | ") for x in f.readlines()]
        data = [[list(map(int,x.replace("  "," ").strip().split(" "))),list(map(int,y.replace("  "," ").strip().split(" ")))] for x,y in data]

    d = {x+1:1 for x in range(len(data))}
    for i, (left, right) in enumerate(data):
        score = 0
        for each in left:
            if each in right:
                score += 1
        if score > 0:
            for ii in range(score):
                d[i+ii+1+1] += d[i+1]

    return sum(d.values())

a1 = p1()
print(f"part 1: {a1}")
a2 = p2()
print(f"part 2: {a2}")

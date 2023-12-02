from math import prod
def p1():
    with open("input.txt", "r") as f:
        raw = f.readlines()

    cap = {
        'red': 12,
        'green': 13,
        'blue': 14
    }
    
    log = 0
    for i, line in enumerate(raw):
        _, line = line.strip().split(": ")
        win = True
        for draw in line.split("; "):
            for turn in draw.split(", "):
                count, color = turn.split(" ")
                if int(count) > cap[color]:
                    win = False
        if win:
            log += i+1
    
    return log
            
def p2():
    with open("input.txt", "r") as f:
        raw = f.readlines()
    
    power = 0
    for i, line in enumerate(raw):
        _, line = line.strip().split(": ")
        cap = {
            'red': 0,
            'green': 0,
            'blue': 0
        }
        for draw in line.split("; "):
            for turn in draw.split(", "):
                count, color = turn.split(" ")
                cap[color] = max(cap[color], int(count))
        power += prod(list(cap.values()))
    return power




answer = p1()
print(f"Part 1: {answer}")
answer = p2()
print(f"Part 2: {answer}")

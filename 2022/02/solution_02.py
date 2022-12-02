with open("input.txt") as f:
    data = [x.split() for x in f.readlines()]

movemap = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z',
}
action = {
    'X': 'L',
    'Y': 'D',
    'Z': 'W',
}
winmap = {
    'X': 'Z', 
    'Z': 'Y', 
    'Y': 'X'  
}
losemap = {v:k for k,v in winmap.items()}
scoredict = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}

def p1(data):
    score = 0
    for them, me in data:
        them = movemap[them]
        if me == them:
            score += scoredict[me] + 3
        elif me+them in ['XZ', 'ZY', 'YX']:
            score += scoredict[me] + 6
        else:
            score += scoredict[me]
    return score

def p2(data):
    score = 0
    for them, me in data:
        them = movemap[them]
        outcome = action[me]
        if outcome == "D":
            score += scoredict[them] + 3
        elif outcome == "L":
            score += scoredict[winmap[them]]
        else:
            score += scoredict[losemap[them]] + 6
    return score

print(f"p1: {p1(data)}")
print(f"p2: {p2(data)}")
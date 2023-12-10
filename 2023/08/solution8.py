from math import lcm

def parse():
    with open("input.txt", "r") as f:
        raw = f.readlines()

    instructions = raw.pop(0).strip()
    _ = raw.pop(0)

    tree = {}
    for line in raw:
        key, nodes = line.split(" = ")
        nodes = nodes.strip().replace("(", "").replace(")", "")
        nodea, nodeb = nodes.split(", ")
        tree[key] = (nodea, nodeb)

    return instructions, tree

def p1():
    instructions, tree = parse()

    dirmap = {"L": 0, "R": 1}

    instructions = instructions * 500
    head = "AAA"
    for i, instruction in enumerate(instructions):
        head = tree[head][dirmap[instruction]]
        if head == "ZZZ":
            return i+1
        
    return "FUCK"

def p2():
    instructions, tree = parse()

    dirmap = {"L": 0, "R": 1}

    instructions = instructions * 5_000_000

    heads = [x for x in tree.keys() if x[-1] == "A"]
    
    results = {}
    for head in heads:
        i = 0
        while True:
            head = tree[head][dirmap[instructions[i]]]
            if head[-1] == "Z":
                results[head] = i + 1
                break
            i += 1
        
    return lcm(*list(results.values()))

a1 = p1()
print(f"Part 1: {a1}")
a2 = p2()
print(f"Part 2: {a2}")
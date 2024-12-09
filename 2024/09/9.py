from copy import deepcopy

def done(memory):
    switches = 0
    for i in range(len(memory)-1):
        if (memory[i] != ".") & (memory[i+1] == "."):
            switches += 1
        if (memory[i] == ".") & (memory[i+1] != "."):
            switches += 1
    return switches == 1

def part1():
    with open("input.txt", "r") as f:
        data = [x.strip() for x in f.readlines()][0]

    memory = []
    i = 0
    for flag, each in enumerate(data):
        each = int(each)
        if flag % 2 == 0:

            memory += [str(i) for _ in range(each)]
            i += 1
        else:
            memory += ["." for _ in range(each)]

    new_memory = deepcopy(memory)
    for i in range(len(new_memory)):
        if i == len(new_memory):
            break
        if new_memory[i] == ".":
            while True:
                maybe = memory.pop(-1)
                _ = new_memory.pop(-1)
                if maybe != ".":
                    break
            new_memory[i] = maybe
        else:
            continue


    return sum([x*int(y) for x,y in enumerate(new_memory)])

print(f"part 1: {part1()}")
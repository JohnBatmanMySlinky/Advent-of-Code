from copy import deepcopy
from collections import defaultdict

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

def count_spaces(board, start):
    spaces = 0
    i = 0
    while i + start < len(board):
        if board[i+start] == ".":
            spaces += 1
        else:
            return spaces
        i += 1
    return spaces

def part2():
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

    addresses = defaultdict(int)
    for each in memory:
        if each != ".":
            addresses[int(each)] += 1

    new_memory = deepcopy(memory)
    while addresses:
        current = max(addresses.keys())
        print(current, addresses[current])
        for i in range(len(new_memory)):
            if new_memory[i] == ".":
                free = count_spaces(new_memory, i)
                if addresses[current] <= free:
                    print(f"\t{free}")
                    new_memory = [x for x in new_memory if x != str(current)]
                    for ii in range(addresses[current]):
                        new_memory[i+ii] = str(current)
                    
                
                break
        addresses.pop(current)
        print(new_memory)
        input()

print(f"part 1: {part1()}")
print(f"part 2: {part2()}")
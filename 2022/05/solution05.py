import re
from copy import deepcopy

with open("input.txt") as f:
    instructions_raw = [x.replace('\n', '') for x in f.readlines()]
    winner = 0
    for i, each in enumerate(instructions_raw):
        if each == '':
            winner = i
    instructions_tmp = instructions_raw[(winner+1):]
    cargo_raw = instructions_raw[:winner]

def parse_cargo(cargo_raw):
    cargo = {}
    for container in cargo_raw[-1]:
        if container != ' ':
            cargo[int(container)] = []
    cargo_raw.pop(-1)

    for line in reversed(cargo_raw):
        for i in range(len(cargo.keys())):
            if line[1+i*4] != ' ':
                cargo[i+1] += [line[1+i*4]]
    return cargo

def parse_instructions(instructions_tmp):
    return [list(map(int,re.findall(r'-?\d+',x))) for x in instructions_tmp]

def p1(cargo_raw, instructions_tmp):
    cargo = parse_cargo(cargo_raw)
    instructions = parse_instructions(instructions_tmp)

    for rng, fromm, to in instructions:
        for _ in range(rng):
            cargo[to] += [cargo[fromm].pop(-1)]

    answer = ''
    for i in range(len(cargo.keys())):
        answer += cargo[i+1].pop(-1)

    return answer

def p2(cargo, instructions):
    cargo = parse_cargo(cargo_raw)
    instructions = parse_instructions(instructions_tmp)

    for rng, fromm, to in instructions:
        cargo[to] += cargo[fromm][-rng:]
        for _ in range(rng):
            cargo[fromm].pop(-1)

    answer = ''
    for i in range(len(cargo.keys())):
        answer += cargo[i+1].pop(-1)

    return answer


print(f"part 1: {p1(deepcopy(cargo_raw), deepcopy(instructions_tmp))}")
print(f"part 2: {p2(deepcopy(cargo_raw), deepcopy(instructions_tmp))}")
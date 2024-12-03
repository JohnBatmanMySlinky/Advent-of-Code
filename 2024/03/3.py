import re

def p1():
    with open("input.txt", "r") as f:
        datas = f.readlines()

    answers = []
    pattern = r"mul\([0-9]{1,3},[0-9]{1,3}\)"
    for data in datas:
        matches = re.findall(pattern, data)
        for match in matches:
            match = match.replace("mul(", "").replace(")", "")
            tmp = list(map(int,match.split(",")))
            assert len(tmp) == 2
            answers += [tmp[0]*tmp[1]]

    return sum(answers)

def p2():
    with open("input.txt", "r") as f:
        datas = f.readlines()

    answers = []
    pattern = r"mul\([0-9]{1,3},[0-9]{1,3}\)|don\'t\(\)|do\(\)"
    do = True
    for data in datas:
        matches = re.findall(pattern, data)
        for match in matches:
            if match == "do()":
                do = True
            elif match == "don't()":
                do = False
            
            if do and match not in ("do()", "don't()"):
                match = match.replace("mul(", "").replace(")", "")
                tmp = list(map(int,match.split(",")))
                assert len(tmp) == 2
                answers += [tmp[0]*tmp[1]]

    return sum(answers)

print(f"part1: {p1()}")
print(f"part2: {p2()}")
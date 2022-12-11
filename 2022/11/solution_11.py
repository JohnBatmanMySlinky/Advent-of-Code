import re
import operator
from collections import defaultdict

with open("input.txt") as f:
    data = [x.split('\n') for x in f.read().split("\n\n")]

def parse(data):
    newdata = []
    for each in data:
        tmp = {}
        tmp["monkey"] = int(re.findall(r'\d+', each[0])[0])
        tmp["items"] = [int(x) for x in re.findall(r'\d+', each[1])]
        assert "new = old" in each[2]
        tmp["operation"] = each[2].strip().split()[-2]
        assert tmp["operation"] in math.keys()
        tmp["operation_num"] = each[2].strip().split()[-1]
        assert "divisible" in each[3]
        tmp["divisible"] = int(re.findall(r'\d+', each[3])[0])
        assert "true" in each[4]
        assert "false" in each[5]
        tmp["true"] = int(re.findall(r'\d+', each[4])[0])
        tmp["false"] = int(re.findall(r'\d+', each[5])[0])
        newdata.append(tmp)
    return newdata

math = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}

def p12(data, rounds, B):
    log = defaultdict(int)
    instructions = parse(data)
    for r in range(rounds):
        for i in range(len(instructions)):
            for item in instructions[i]["items"]:
                log[i] += 1
                if instructions[i]["operation_num"] == "old":
                    new = math[instructions[i]["operation"]](item, item) // 3
                else:
                    new = math[instructions[i]["operation"]](item, int(instructions[i]["operation_num"])) // B

                if new % instructions[i]["divisible"] == 0:
                    instructions[instructions[i]["true"]]["items"].append(new)
                    # print(f"{i} --> {new} --> {instructions[i]['true']}")
                else:
                    instructions[instructions[i]["false"]]["items"].append(new)
                    # print(f"{i} --> {new} --> {instructions[i]['false']}")

            instructions[i]["items"] = []

        if r % 100 == 0:
            print(f"  iteration: {r}")

        # for i in range(len(instructions)):
            # print(f"{r}: {i}: {instructions[i]['items']}")
    a, b = sorted(log.values())[-2:]
    return a*b

print(f"part 1: {p12(data, 20, 3)}")
print(f"part 2: {p12(data, 10_000, 1)}")
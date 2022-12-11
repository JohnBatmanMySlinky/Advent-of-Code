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

    K = 1
    for each in instructions:
        K *= each["divisible"]

    for r in range(rounds):
        for i in range(len(instructions)):
            for item in instructions[i]["items"]:
                log[i] += 1
                if instructions[i]["operation_num"] == "old":
                    new = math[instructions[i]["operation"]](item, item) // B
                else:
                    new = math[instructions[i]["operation"]](item, int(instructions[i]["operation_num"])) // B

                # (a mod kn) mod n ≡ a mod n for all integer k
                # lmao @ natively trying that...
                # those old * old get big fast...
                new %= K

                if new % instructions[i]["divisible"] == 0:
                    instructions[instructions[i]["true"]]["items"].append(new)
                else:
                    instructions[instructions[i]["false"]]["items"].append(new)

            instructions[i]["items"] = []

    a, b = sorted(log.values())[-2:]
    return a*b

print(f"part 1: {p12(data, 20, 3)}")
print(f"part 2: {p12(data, 10_000, 1)}")
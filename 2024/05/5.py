from collections import defaultdict
from itertools import permutations

def parse():
    with open("input.txt", "r") as f:
        data = [x.strip() for x in f.readlines()]

    keys = defaultdict(set)
    lines = []
    for line in data:
        if "|" in line:
            k,v = line.split("|")
            keys[int(k)].add(int(v))
        elif "," in line:
            lines += [[int(x) for x in line.split(",")]]

    return keys, lines

def ordered_ok(keys, line):
    ok = True
    seen = {-1}
    for i,each in enumerate(line):
        if (i == len(line)-1)and(each not in keys.keys()):
            continue
        else:
            if any([x in seen for x in keys.get(each, [-1])]):
                ok = False
            else:
                seen.add(each)
    
    return ok
        

def part1():
    keys, lines = parse()

    answer = 0
    for line in lines:
        ok = ordered_ok(keys, line)

        if ok:
            answer += line[len(line) // 2]

    return answer

def part2():
    keys, lines = parse()

    answer = 0
    for idx, line in enumerate(lines):
        ok = ordered_ok(keys, line)

        if not ok:
            print(f"{idx/len(lines):.2%}")
            perms = permutations(line)
            for perm in perms:
                ok = ordered_ok(keys, perm)
                if ok:
                    answer += perm[len(perm) // 2]
                    break


    return answer


print(f"part1 : {part1()}")
print(f"part2 : {part2()}")
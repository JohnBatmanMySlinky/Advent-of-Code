def part1():
    with open("input.txt", "r") as f:
        left = []
        right = []
        for line in f.readlines():
            l, r = line.strip().split("   ")
            left += [int(l)]
            right += [int(r)]
    
    left = sorted(left)
    right = sorted(right)

    answer = 0
    for l,r in zip(left, right):
        answer += abs(l - r)

    return answer

def part2():
    with open("input.txt", "r") as f:
        left = []
        right = []
        for line in f.readlines():
            l, r = line.strip().split("   ")
            left += [int(l)]
            right += [int(r)]

    counts = {}
    for r in right:
        if r in counts.keys():
            counts[r] += 1
        else:
            counts[r] = 1


    answer = 0
    for l in left:
        answer += l * counts.get(l, 0)

    return answer

print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
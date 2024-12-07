from itertools import product
from functools import reduce
from operator import add, mul

def reducer(acc, pair):
    num, op = pair
    return op(acc, num)

def dumb(a,b):
    return int(str(a)+str(b))

def part(ops):
    with open("input.txt", "r") as f:
        data = [x.strip() for x in f.readlines()]

    answer = 0 
    for line in data:
        target, tmp = line.split(": ")
        N = tmp.count(" ")
        target = int(target)
        numbers = [int(x) for x in tmp.split(" ")]
        combos = list(product(ops, repeat=N))
        for combo in combos:
            maybe = reduce(reducer, zip(numbers[1:], combo), numbers[0])
            if maybe == target:
                answer += target
                break
    return answer

print(f"part 1: {part([mul, add])}")
print(f"part 2: {part([mul, add, dumb])}")
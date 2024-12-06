def part1():
    with open("input.txt", "r") as f:
        data = [x.strip() for x in f.readlines()]

    return f

print(f"part 1: {part1()}")
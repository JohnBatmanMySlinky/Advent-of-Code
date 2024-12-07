def part1():
    with open("input.txt", "r") as f:
        data = list(f.readlines()[0])

    answer = 0
    new_data = data + [data[0]]
    while new_data:
        current = new_data.pop(0)
        if new_data:
            if current == new_data[0]:
                answer += int(current)

    return answer

def part2():
    with open("input.txt", "r") as f:
        data = list(f.readlines()[0])

    answer = 0
    new_data = data + [data[0]]
    i = 0
    while new_data:
        current = new_data.pop(0)
        if new_data:
            if current == data[(i + len(data)//2)%len(data)]:
                answer += int(current)
        i += 1

    return answer

print(f"part 1: {part1()}")
print(f"part 2: {part2()}")
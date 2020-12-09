import sys

dat = [x.replace('\n','').split(' ') for x in sys.stdin]

# part 1
idx = 0
accumulator = 0
executed = set()
while True:
    op = dat[idx][0]
    arg = int(dat[idx][1])

    if op == "acc":
        accumulator += arg
        idx += 1

    if op == "jmp":
        idx += arg

    if op == "nop":
        idx += 1

    if idx in executed:
        break

    executed.add(idx)
print(accumulator)

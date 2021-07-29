with open(r"input.txt","r") as f:
    dat = [int(x) for x in f.readlines()]

# part 1
print(sum([x//3-2 for x in dat]))


# part 2
fin = 0
for x in dat:
    while x//3-2 > 0:
        fin += x//3-2
        x = x//3-2
print(fin)
with open(r'input.txt','r') as f:
    dat = [list(x.replace('\n','')) for x in f.readlines()]

def count_trees_hit(ls, right, down):
    position = 1
    trees_hit = 0
    rep = len(ls[0])
    for row in range(0,len(ls),down):
        if ls[row][(position % rep)-1] == '#':
            trees_hit += 1
        position += right
    return(trees_hit)

# part 1
print(count_trees_hit(dat,3,1))


# part 2
answer = 1
for slopes in [[1,1], [3,1], [5,1], [7,1],[1,2]]:
    answer *= count_trees_hit(dat,slopes[0],slopes[1])
print(answer)

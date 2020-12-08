with open('input.txt', 'r') as f:
    dat = []
    for r in f.readlines():
        r = r.replace('\n','')
        r = r.replace('bags','bag')
        r = r.replace(',','')
        r = r.replace('.','')
        r = r.replace(' contain','')
        r = r.replace(' no ',' 0 no ')
        r = r.split(' ')
        dat.append(r)


# more parsing
TREE = {}
for r in dat:
    parent = '_'.join(r[:3])
    children = []
    number_of_children = []
    for x in range(4, len(r)+1, 4):
        child = '_'.join(r[x:x+3])
        if child != 'no_other_bag':
            children.append(child)
        
        number_of_children.append((child,int(r[x-1])))
    TREE[parent] = number_of_children


# tree traversal for part 1
def node_has_shinygold(node): #BREADTH FIRST SEARCH
    visited = [node]
    q = [node]
    has_gold = 0
    tot_bags = 1
        
    while q:
        s = q.pop(0)
        if s == 'shiny_gold_bag':
            has_gold += 1
        if s == 'no_other_bag':
            continue 
        for neighbor, cnt in TREE[s]:
            if neighbor not in visited:
                visited.append(neighbor)
                q.append(neighbor)
    return(has_gold, tot_bags)

# part 1 answer
answer1 = 0
for k in TREE.keys():
    if k != 'shiny_gold_bag':
        answer1 += node_has_shinygold(k)[0]
print('part1: ' + str(answer1))
print('----------------------------------------------------------------------')

# part 2 answer
def number_of_bags_in(node):    #DEPTH FIRST SEARCH
    tot_count = 0
    for neighbor, cnt in TREE[node]:
        tot_count += cnt
        if neighbor == 'no_other_bag':
            continue
        tot_count += cnt * number_of_bags_in(neighbor)
    return(tot_count)
print('part2: ' + str(number_of_bags_in('shiny_gold_bag')))


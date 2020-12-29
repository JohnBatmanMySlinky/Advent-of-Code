with open(r'input.txt', 'r') as f:
    dat = [x[:-1].replace('-', ' ').replace(':', '').split(' ') for x in f.readlines()]

def part1(lower, upper, T, pwd):
    letter_count = sum([1 for x in pwd if x == T])
    return(int(lower) <= letter_count <= int(upper)) 

def part2(p1, p2, T, pwd):
    x = pwd[int(p1)-1] == T
    y = pwd[int(p2)-1] == T
    return(x+y == 1)

answer1 = 0
answer2 = 0
for each in dat:
    answer1 += 1 * part1(each[0], each[1], each[2], each[3])
    answer2 += 1 * part2(each[0], each[1], each[2], each[3])
print(answer1)
print(answer2)

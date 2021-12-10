with open('input.txt') as f:
    dat = [x.strip() for x in f.readlines()]

rev_dict = {
    '}': '{',
    ']':'[',
    ')':'(',
    '>':'<',
}

score_dict = {
    '}': 1197,
    ']': 57,
    ')': 3,
    '>': 25137,
}

def part1(dat):
    score = 0
    for i,row in enumerate(dat):
        stack = []
        for each in row:
            stack.append(each)
            if each not in ['[', '(', '{', '<']:
                s = stack.pop()
                if rev_dict[s] != stack[-1]:
                    score += score_dict[s]
                    break
                else:
                    stack.pop()
    return score


score2_dict = {
    '{': 3,
    '[': 2,
    '(': 1,
    '<': 4,
}
def part2(dat):
    score = []
    for i,row in enumerate(dat):
        broke = False
        tmp_score = 0
        stack = []
        for each in row:
            stack.append(each)
            if each not in ['[', '(', '{', '<']:
                s = stack.pop()
                if rev_dict[s] != stack[-1]:
                    broke = True
                    break
                else:
                    stack.pop()
        
        if not broke:
            for remainder in reversed(stack):
                tmp_score *= 5
                tmp_score += score2_dict[remainder]

            score.append(tmp_score)
    return sorted(score)[len(score)//2]
            

print(part1(dat))
print(part2(dat))
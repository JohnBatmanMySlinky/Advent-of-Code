import sys
import itertools

dat = [x.strip('\n') for x in sys.stdin]

# create rules dict and list of messages
rules = {}
messages = []
for x in dat:
    if x.find(':')>-1:
        rules[int(x.split(':')[0])] = [x.replace('"', '').split(':')[1].strip()]
    else:
        if len(x) > 1:
            messages.append(x)


def make_pattern(rule):
    if rules[rule][0] == 'a' or rules[rule][0] == 'b':
        return rules[rule][0]
    else: 
        parts = rules[rule][0].split(' | ')
        pattern = []
        for part in parts:
            codes = part.split(' ')
            
            # this is terrible
            for x in make_pattern(int(codes[0])):
                
                # if just rule: number, be done
                if len(codes) == 1:
                    pattern.append(''.join([x]))
                    
                # this is where the rest are
                elif len(codes) == 2:
                    for y in make_pattern(int(codes[1])):
                        pattern.append(''.join([x,y]))
                        
                # lmao the example rule 0 is the only three arg rule
                elif len(codes) == 3 and rule == 0:
                    for y in make_pattern(int(codes[1])):
                        pattern.append(''.join([x,y]))
                else:
                    # thank god
                    assert 0>0
        return(pattern)

# part 1
acceptable_patterns = make_pattern(0)
answer = 0
for each in messages:
    if each in acceptable_patterns:
        answer += 1
print('part1: ' + str(answer))
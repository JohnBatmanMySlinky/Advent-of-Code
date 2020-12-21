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
 
    
# part2
# after some sketching the infinite loop has two forms which are able to be accounted for manually
# 0: 8 11
# 8 --> (42), (42 42), (42, 42, 42), ....
# 11 --> (42, 31), (42, 42, 31, 31), (42, 42, 42, 31, 31, 31), ....
fourtytwo = make_pattern(42)
thirtyone = make_pattern(31)

print(fourtytwo)
print(thirtyone)
assert len(fourtytwo) == len(thirtyone)

answer2 = 0
for eight in range(1,5):
    for eleven in range(1,5):
        print('42'*eight + '42'*eleven + '31'*eleven)
        tmp = []
        for x in range(len(fourtytwo)):
            tmp.append(fourtytwo[x]*eight + fourtytwo[x]*eleven + thirtyone[x]*eleven)
        for each in messages:
            if each in tmp:
                answer2 += 1
print('part2: ' + str(answer2))
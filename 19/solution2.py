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
assert len(fourtytwo) == len(thirtyone)

# for each message we can back into a combination of 42's and 31's and check if it fits the above pattern
# first build out valid combos
valid_combos = []
for x in range(1,50):
    for y in range(1,50):
        valid_combos.append('F'*x + 'F'*y + 'T'*y)

# then build combo for each message and check validity
answer2 = 0
for each in messages:
    # build combo of F & T's
    chunk_len = len(fourtytwo[0])
    message_len = len(each)
    combo = ''
    if message_len % chunk_len != 0:
        continue
    else:
        for x in range(chunk_len, message_len+chunk_len, chunk_len):
            if each[x-chunk_len:x] in fourtytwo:
                combo += 'F'
            if each[x-chunk_len:x] in thirtyone:
                combo += 'T'

    #check combo is valid
    if combo in valid_combos:
        answer2 += 1

print('part2: ' + str(answer2))
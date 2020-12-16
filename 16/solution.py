import sys
from collections import defaultdict

dat = [x[x.find(':')+1:].strip(' ').strip('\n').replace(' or ', '-').replace(',','-').split('-') for x in sys.stdin]

notes = []
ticket = []
nearby = []

i = 0
cnt = 0
while i < len(dat):
    if dat[i] == ['']:
        cnt += 1
        i += 2
    if cnt == 0:
        notes.append(dat[i])
        i +=1
    if cnt == 1:
        ticket.append(dat[i])
        i +=1
    if cnt == 2:
        nearby.append(dat[i])
        i +=1
    
# all valid seats
valid = set()
for n in notes:
    [valid.add(x) for x in range(int(n[0]), int(n[1])+1)]
    [valid.add(x) for x in range(int(n[2]), int(n[3])+1)]

# determining which seats are invalid
invalid = []
remain = []
for x in nearby:
    valid_ind = 0
    for y in x:
        if int(y) not in valid:
            valid_ind += 1
            invalid.append(int(y))
    if valid_ind == 0:
        remain.append(x)
print('part1: ' + str(sum(invalid)))

# you know it's AWFUL when i start adding comments
# departures are the top 6 rows
departures = {}
for i,n in enumerate(notes):
    tmp = set()
    [tmp.add(x) for x in range(int(n[0]), int(n[1])+1)]
    [tmp.add(x) for x in range(int(n[2]), int(n[3])+1)]
    departures[i] = tmp

# loop through each POSITION
answer_dict = defaultdict(list)
for p in range(len(ticket[0])):
    # build list containing all first positions
    pos = []
    for r in remain:
        pos.append(int(r[p]))
    
    # confirm all first positions are a given departure
    for k,v in departures.items():
        if all([x in v for x in pos]):
            # key is index along ticket
            # value is which depature
            answer_dict[p].append(k)

# now to identify unique solutions
def maxlen(d): return(max([len(v) for k,v in d.items()]))

DONE = set()
while maxlen(answer_dict) > 1:
    for k1, v1 in answer_dict.items():
        if len(v1) == 1 and v1[0] not in DONE:
            DONE.add(v1[0])
            for k2, v2, in answer_dict.items():
                if v1[0] in v2 and len(v2) > 1:
                    v2.remove(v1[0])

# answer_dict values 0-5 are the 6 departures
# look up keys corresponding to values 0-5
# using those keys index the ticket and product the numbers
answer = 1
for k,v in answer_dict.items():
    if v[0] < 6:
        answer *= int(ticket[0][k])
print('part2: ' + str(answer))
    

    
        
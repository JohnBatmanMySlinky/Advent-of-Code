import sys


dat = [x.split('\n')[1:] for x in sys.stdin.read().split('\n\n')]
p1 = [int(x) for x in dat[0]]
p2 = [int(x) for x in dat[1]]

def update_deck(a,b):
    '''
    assuming a won
    '''
    a.append(a.pop(0))
    a.append(b.pop(0))
    return(a,b)

def calc_score(a,b):
    '''
    given two hands, picks the winner and returns their score
    '''
    if len(b) == 0:
        winner = a
    elif len(a) == 0:
        winner = b
    else:
        print('no winners yet')
        assert 0 > 0

    winner = [x for x in reversed(winner)]
    score = sum([winner[i]*(i+1) for i in range(len(winner))])

    return(score)

# play!
round = 0
while p1 and p2:
    round += 1
    if p1[0] > p2[0]:
        p1, p2 = update_deck(p1, p2)
    else:
        p2, p1 = update_deck(p2, p1)

print('part1: ' + str(calc_score(p1, p2)))
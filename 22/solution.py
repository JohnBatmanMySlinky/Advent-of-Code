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


############## p2
p1 = [int(x) for x in dat[0]]
p2 = [int(x) for x in dat[1]]

def play(a, b, C):
    played_deck = set()
    while a and b:
        C += 1
        if C % 100000 == 0:
            # print(C)
            pass
        # check to see if played
        t = (tuple(a), tuple(b))
        if t in played_deck:
            # winind and winner
            return(1,a,C)
        else:
            played_deck.add(t)

            # continue
            aa = a.pop(0)
            bb = b.pop(0)
            if aa > len(a) or bb > len(b):
                if aa > bb:
                    winner = a
                    winind = 1
                elif aa < bb:
                    winner = b
                    winind = 2
                else:
                    assert 5 == 6
            else:
                # play subgame so see who one, don't do anything with resulting hand
                # whole point of winind is pass winner and NOT MODIFY hand
                # I CAN'T READ....ughhhhh
                # ONLY PASS THE NUMBER OF CARDS EQUAL TO AA / BB
                winind, _, C = play(a[:aa], b[:bb], C)

                if winind == 1:
                    winner = a
                elif winind == 2:
                    winner = b
                else:
                    assert 5 == 6

        if winind == 1:
            winner.append(aa)
            winner.append(bb)
        elif winind == 2:
            winner.append(bb)
            winner.append(aa)
        else:
            assert 5 == 6

    return(winind, winner, C)

pls = 0
i,w,PLS = play(p1,p2, pls)
print('part2: ' + str(calc_score(w,[])))
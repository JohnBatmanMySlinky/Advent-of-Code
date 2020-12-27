import sys

hand = [int(x) for x in sys.stdin.read()]

ROUNDS = 100
cards = len(hand)
current_idx = 0
for _ in range(ROUNDS):
    # whats the current card
    current = hand[current_idx]

    # pick up three cards
    pickup = []
    [pickup.insert(0,hand[(current_idx+pu+1)%cards]) for pu in range(3)]

    # pop these from hand for a bit
    [hand.remove(x) for x in pickup]

    # destination
    destination = current - 1
    if destination == 0:
        destination = 9
    while destination in pickup:
        destination -=  1
        if destination == 0:
            destination = 9
    print(destination)
    print('-------------------')

    # place picked up cars back in hand based on destination
    [hand.insert(hand.index(destination)+1,pickup[i]) for i in range(3)]

    # now move current index (noting current_idx has changed since u popped stuff)
    current_idx = (hand.index(current) + 1)%cards

loc = hand.index(1)
print(''.join([str(x) for x in hand[loc+1:]+hand[:loc]]))




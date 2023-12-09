def parse():
    with open("input.txt", "r") as f:
        raw = [(x.strip().split(" ")[0], int(x.strip().split(" ")[1])) for x in f.readlines()]
    return raw

def score(hand):
    # print(f"Hand: {hand}")
    answer = -1
    if fiveofakind(hand):
        answer = 7
    elif fourofakind(hand):
        answer = 6
    elif fullhouse(hand):
        answer = 5
    elif threeofakind(hand):
        answer = 4
    elif twopair(hand):
        answer = 3
    elif onepair(hand):
        answer = 2
    elif highcard(hand):
        answer = 1
    else:
        assert False
    # print(f"Score: {answer}\n")
    return answer


def fiveofakind(hand):
    a, b, c, d, e = hand
    return a == b == c == d == e

def fourofakind(hand):
    a, b, c, d, e = sorted(hand)
    return (hand.count(a) == 4) | (hand.count(e) == 4)

def fullhouse(hand):
    a, b, c, d, e = sorted(hand)
    return ((hand.count(a) == 3) & (hand.count(e) == 2)) | ((hand.count(a) == 2) & (hand.count(e) == 3))

def threeofakind(hand):
    a, b, c, d, e = sorted(hand)
    return ((hand.count(a) == 3) | (hand.count(b) == 3) | (hand.count(c) == 3) | (hand.count(d) == 3) | (hand.count(e) == 3)) & (len(set(hand)) == 3)

def twopair(hand):
    # ONLY WORKS BECAUSE OF ORDER OF IFS
    return len(set(hand)) == 3

def onepair(hand):
    # ONLY WORKS BECAUSE OF ORDER OF IFS
    return len(set(hand)) == 4

def highcard(hand):
    # ONLY WORKS BECAUSE OF ORDER OF IFS
    return len(set(hand)) == 5

scorer_dict = {x: chr(i+97) for i,x in enumerate(reversed(["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]))}

def remaphand(hand):
    return "".join([scorer_dict[x] for x in hand])


def p1():
    data = parse()
    results = []
    for hand, bid in data:
        results.append({"score": score(hand), "hand": hand, "remappedhand": remaphand(hand), "bid": bid})
    
    final_list = []
    for X in reversed(range(1,8)):
        results_tmp = [x for x in results if x["score"] == X]
        results_tmp = sorted(results_tmp, key = lambda x : x["remappedhand"])
        if results_tmp:
            final_list += results_tmp

    final_list = list(reversed(final_list))
    FIN = 0
    for i in range(len(final_list)):
        FIN += final_list[i]["bid"] * (i + 1)

    return FIN

a1 = p1()
print(f"Part 1: {a1}")
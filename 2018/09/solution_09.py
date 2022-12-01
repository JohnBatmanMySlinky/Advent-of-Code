from collections import defaultdict, deque
import re

with open("input.txt", "r") as f:
    inputs = re.findall(r'\d+', f.readlines()[0])

players = int(inputs[0])
rounds = int(inputs[1])

def play(rounds, players):
    d = deque([0])
    score_dict = defaultdict(int)
    for i in range(1,rounds+1):
        score = 0
        if i % 23 == 0:
            d.rotate(7)
            score += i + d.pop()
            d.rotate(-1)
        else:
            d.rotate(-1)
            d.append(i)
        score_dict[i%players] += score
    return max(score_dict.values())



winner = play(rounds, players)
print(f"part 1: {winner}")

winner = play(rounds*100, players)
print(f"part 2: {winner}")
        
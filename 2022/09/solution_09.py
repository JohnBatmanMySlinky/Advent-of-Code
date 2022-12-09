with open("input.txt") as f:
    data = [x.strip().split() for x in f.readlines()]

def p12(data, knots):
    T = [[0,0] for DINGDONG in range(knots)]
    visited = set()
    for direction, amount in data:
        for steps in range(int(amount)):
            if direction == "U":
                T[0][1] += 1
            elif direction == "D":
                T[0][1] -= 1
            elif direction == "L":
                T[0][0] -= 1
            elif direction == "R":
                T[0][0] += 1

            for k in range(knots-1):
                if (abs(T[k][0] - T[k+1][0])>1) | (abs(T[k][1] - T[k+1][1])>1):
                    T[k+1][0] += min(1,max(-1, T[k][0] - T[k+1][0]))
                    T[k+1][1] += min(1,max(-1, T[k][1] - T[k+1][1]))
                    
            visited.add(tuple(T[-1]))
    return len(visited)
        
print(f"part 1: {p12(data, 2)}")
print(f"part 2: {p12(data, 10)}")
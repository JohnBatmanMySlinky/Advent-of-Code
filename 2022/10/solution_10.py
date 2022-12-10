with open("input.txt") as f:
    data = [x.strip() for x in f.readlines()]

def p1(data, dumblist):
    new = []
    for each in data:
        if each == "noop":
            new.append(each)
        else:
            a, b = each.split()
            new.append(f"{a} {0}")
            new.append(f"{a} {b}")

    X = 1
    cycle = 1
    answer = 0 
    while dumblist:
        for each in new:
            if cycle in dumblist:
                dumblist.remove(cycle)
                answer += cycle * X
            if each == "noop":
                pass
            elif each.split()[1] == "0":
                pass
            else:
                b = int(each.split()[1])
                X += b
            cycle += 1
    return answer

    
def p2(data):
    new = []
    for each in data:
        if each == "noop":
            new.append(each)
        else:
            a, b = each.split()
            new.append(f"{a} {0}")
            new.append(f"{a} {b}")

    board = [["." for x in range(40)] for _ in range(6)]
    # board = ["." for x in range(240)]
    sprite = [1,2,3]
    X = 1
    cycle = 1
    answer = 0 
    for each in new:
        # update sprite
        sprite = [X-1, X, X+1]
      
        # begin write
        if (cycle-1)%40 in sprite:
            i = (cycle-1)//40
            board[i][(cycle-1)%40] = "#"

        if each == "noop":
            pass
        elif each.split()[1] == "0":
            pass
        else:
            b = int(each.split()[1])
            X += b

        cycle += 1
    return board
    


print(f"part 1: {p1(data, [20, 60, 100, 140, 180, 220])}")
print(f"part 2: {p2(data)}")
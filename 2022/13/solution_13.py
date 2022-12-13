with open("input.txt") as f:
    data = [[eval(y) for y in x.split('\n')] for x in f.read().split('\n\n')]

def compare(x,y, promoted):
    # if the lists are same length
    for i in range(max(len(x), len(y))+1):
        # input()
        if (i >= len(x)) & (i >= len(y)):
            print("E")
            print("True")
            return True
        elif (i >= len(x)) & promoted:
            print("SP")
            print("TRUE")
            return False
        elif (i >= len(y)) & promoted:
            print("SP")
            print("True")
            return True
        if (i >= len(x)) & (not promoted):
            print("SP")
            print("TRUE")
            return True
        elif (i >= len(y)) & (not promoted):
            print("SP")
            print("True")
            return False
        elif isinstance(x[i],list) & isinstance(y[i],list):
            print("L, L")
            return compare(x[i], y[i], False)
        elif isinstance(x[i],list) & (not isinstance(y[i],list)):
            print("L, NL")
            return compare(x[i],[y[i]], True)
        elif (not isinstance(x[i], list)) & isinstance(y[i], list):
            print("NL", "L")
            return compare([x[i]], y[i], True)
        else: 
            if x[i] > y[i]:
                print("FALSE")
                return False

def p1(data):
    winners = []
    for i,(a,b) in enumerate(data):
        print(a,b)
        FINAL = compare(a,b, False)
        print(f"FINAL: {FINAL}")
        if FINAL:
            print(f"     {i}")
            winners.append(i+1)
    return sum(winners)


print(f"part 1: {p1(data)}")
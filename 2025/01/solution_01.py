with open("input.txt", "r") as f:
    data = f.readlines()
    mapper = {"L": -1, "R": 1}
    data = [([mapper[x[0]], int(x[1:])]) for x in data]

START = 50

def p1(data):
    number = START
    counter = 0
    for sign, turn in data:
        number = (number + (sign * turn)) % 100
    
        if number == 0:
            counter += 1
        
    return counter


def rotate(number, orig_number, sign, turn, counter):
    number = (number + (sign * turn))

    if ((number > 100) | (number < 0)) & (orig_number != 0):
        counter += 1

    number = number % 100

    if number == 0:
        counter += 1

    return number, counter

def p2(data):
    number = START
    counter = 0
    for sign, turn in data:
        orig_number = number

        if turn < 100:
            turn_full = 0
            turn_remainder = turn
        else:
            turn_full = turn // 100
            turn_remainder = turn - turn_full * 100

        for each in range(turn_full):
            number, counter = rotate(number, orig_number, sign, 100, counter)
        
        number, counter = rotate(number, orig_number, sign, turn_remainder, counter)
        
    return counter

answer = p1(data)
print(f"Solution d1p1: {answer}")

answer = p2(data)
print(f"Solution d1p2: {answer}")

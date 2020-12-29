import sys

dat = [x.replace('\n','').split(' ') for x in sys.stdin]

# part 2
def play_game(game):
    idx = 0
    accumulator = 0
    executed = set()
    while True:
        if idx == len(game):
            return(accumulator)
        op = dat[idx][0]
        arg = int(dat[idx][1])

        if idx in executed:
                return(0)
        else:
            executed.add(idx)


        if op == "nop":
            idx += 1
        elif op == "acc":
            accumulator += arg
            idx += 1
        else:
            idx += arg
    return(accumulator)   
    
    
# fix the program by changing a nop --> jmp or a jmp --> nop
for i,r in enumerate(dat):
    if r[0] == "jmp":
        dat[i][0] = "nop"
        game_out = play_game(dat)
        if game_out > 0:
            print('part2: ' + str(game_out))
            break
        else:
            dat[i][0] = "jmp"
    elif r[0] == "nop":
        dat[i][0] = "jmp"
        game_out = play_game(dat)
        if game_out > 0:
            print('part2: ' + str(game_out))
            break
        else:
            dat[i][0] = "nop"
    else:
        pass
          
        
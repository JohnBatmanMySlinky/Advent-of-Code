import sys
from copy import deepcopy

board1 = [[x for x in y.replace('\n','')] for y in sys.stdin]
board2 = deepcopy(board1)

def play_1(grid):
    newgrid = []
    for row in range(len(grid)):
        newrow = []
        for col in range(len(grid[0])):
            adj = []
            for i in range(-1,2,1):
                for j in range(-1,2,1):
                    if (i==0) & (j==0):
                        continue
                    if row+i in range(len(grid)) and col+j in range(len(grid[0])):
                        adj.append(grid[row+i][col+j])
            # empty and no occupied seats in adjacent --> occupied
            if (grid[row][col] == 'L') & ('#' not in adj):
                newrow.append('#')
            # occupied and 4+ occupied in adj --> empty
            elif (grid[row][col] == '#') & (adj.count('#') >= 4):
                newrow.append('L')
            # else no change
            else:
                newrow.append(grid[row][col])
        newgrid.append(newrow)
    return(newgrid)


# part 1
while True:
    new_board1 = play_1(board1)
    if new_board1 == board1:
        print('part1: ' + str(sum([r.count('#') for r in board1])))
        break
    else:
        board1 = deepcopy(new_board1)
    
###################################################################################

def play_2(grid):
    newgrid = []
    for row in range(len(grid)):
        newrow = []
        for col in range(len(grid[0])):
            adj = []
            for i in range(-1,2,1):
                for j in range(-1,2,1):
                    if (i==0) & (j==0):
                        continue
                    
                    # logic for them diagonals
                    k = 1
                    while row+i*k in range(len(grid)) and col+j*k in range(len(grid[0])):
                        if grid[row+i*k][col+j*k] != ".":             
                            adj.append(grid[row+i*k][col+j*k])
                            break
                        k += 1
                                         
            # empty and no occupied seats in adjacent --> occupied
            if (grid[row][col] == 'L') & ('#' not in adj):
                newrow.append('#')
            # occupied and 4+ occupied in adj --> empty
            # it's 5+ meow
            elif (grid[row][col] == '#') & (adj.count('#') >= 5):
                newrow.append('L')
            # else no change
            else:
                newrow.append(grid[row][col])
        newgrid.append(newrow)
    return(newgrid)


# part 2
while True:
    new_board2 = play_2(board2)
    if new_board2 == board2:
        print('part2: ' + str(sum([r.count('#') for r in board2])))
        break
    else:
        board2 = deepcopy(new_board2)
    
    
    
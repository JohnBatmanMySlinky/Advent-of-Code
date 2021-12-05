with open('input.txt') as f:
    dat = [x.strip().split('\n\n') for x in f.readlines()]
    draws = [int(x) for x in dat[0][0].split(',')]
    dat.pop(0)
    dat.pop(0)

    boards = []
    board = []
    for each in dat:
        if each==['']:
            boards.append(board)
            board = []
        else:
            board.append([int(x) for x in each[0].replace('  ',' ').split(' ')])
    boards.append(board)

def check_winner(board):
    for r in range(len(board)):
        if all([x=='X' for x in board[r]]):
            return True
    for c in range(len(board[0])):
        if all([x[c]=='X' for x in board]):
            return True
    # if all([board[x][x]=='X' for x in range(len(board))]):
    #     print('d1')
    #     return True
    # if all([board[len(board)-1-x][x]=='X' for x in range(len(board))]):
    #     print('d2')
    #     return True
    return False


def update_board(board, X):
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == X:
                board[r][c] = 'X'
    return board

def score_board(board):
    score = 0
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] != 'X':
                score += board[r][c]
    return score

def play(draw, boards):
    previous = 'uhoh'
    round1 = True
    while draw and len(boards)>1:
        current = draw.pop(0)

        # check if there are any winners
        mask = []
        for i in range(len(boards)):
            if not check_winner(boards[i]):
                continue
            else:
                if round1:
                    round1 = False
                    score = score_board(boards[i])
                    print(f"part 1: {previous * score}")
                mask.append(i)

        # turns out more than more board can drop out at a time :)
        boards = [x for i,x in enumerate(boards) if i not in mask]

        # update boards
        for i in range(len(boards)):
            boards[i] = update_board(boards[i],current)

        previous = current
    score = score_board(boards[0])
    print(f"part 2: {previous * score}")

play(draws, boards)





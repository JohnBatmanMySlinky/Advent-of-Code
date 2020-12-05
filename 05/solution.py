with open('input.txt', 'r') as f:
    dat = [x.replace('\n', '') for x in f.readlines()]

def find_seat_ID(ticket):
    row_idx = [0,127]
    for x in ticket[:7]:
        if x == 'F':
            row_idx[1] -= int((row_idx[1] - row_idx[0]) / 2) + 1
        if x == 'B':
            row_idx[0] += int((row_idx[1] - row_idx[0]) / 2) + 1

    col_idx = [0,7]
    for y in ticket[7:]:
        if y == 'L':
            col_idx[1] -= int((col_idx[1] - col_idx[0]) / 2) + 1
        if y == 'R':
            col_idx[0] += int((col_idx[1] - col_idx[0]) / 2) + 1

    assert row_idx[0] == row_idx[1]
    assert col_idx[0] == col_idx[1]
    return(row_idx[0]*8 + col_idx[0])

part1 = 0
part2 = []
for ticket in dat:
    ID = find_seat_ID(ticket)
    part2.append(ID)
    if ID > part1:
        part1 = ID
print('part1: ' + str(part1))


for i, seat in enumerate(sorted(part2)):
    if i+6 != seat:
        break
print('part2: ' + str(i+6))

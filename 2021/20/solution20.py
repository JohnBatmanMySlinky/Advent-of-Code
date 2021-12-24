with open('input.txt') as f:
    raw = [[y.strip() for y in x.split('\n\n')]for x in f.readlines()]
    decipher = []
    image = []
    switch = False
    for each in raw:
        if each == ['']:
            switch = True
        if switch == False:
            decipher += each[0]
        if switch == True and each != ['']:
            image.append(each[0])
    decipher = ''.join(decipher)


def pad(to_pad, N, p):
    for _ in range(N):
        to_pad.insert(0, p*len(to_pad[0]))
        to_pad.append(p*len(to_pad[0]))
        to_pad = [p + x + p for x in to_pad]
    return to_pad


def update(image, decipher, i):
    mapper = {'#': '1', '.': '0'}
    new_image = []
    for y in range(len(image)):
        new_row = ''
        for x in range(len(image[0])):
            binary = ''
            for (j,k) in [(-1,-1), (0,-1), (1,-1), (-1,0), (0,0), (1,0), (-1,1), (0,1), (1,1)]:
                if 0 <= x+j <= len(image)-1 and 0 <= y+k <= len(image)-1:
                    binary += mapper[image[y+k][x+j]]
                else:
                    if decipher[0]=='#' and (i+1)%2==0:
                        infinity='1'
                    else:
                        infinity='0'
                    binary += infinity
            position = int(binary,2)
            new_row += decipher[position]
        new_image.append(new_row)

    return new_image

def part1(image, decipher, N):

    image = pad(image, 60, '.')

    for i in range(N):
        image = update(image, decipher, i)

    score = 0
    for x in image:
        for y in x:
            if y == '#':
                score += 1
    return score
p1 = image.copy()
p2 = image.copy()

print(part1(p1, decipher, 2))
print(part1(p2, decipher, 50))
        
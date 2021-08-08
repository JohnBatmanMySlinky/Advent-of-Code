with open(r"input.txt","r") as f:
    image = [x for x in f.read()]

def parse(image, x, y):
    fin = []
    n_rows = int(len(image) / x)

    fin = []
    layer = []
    for i in range(1,n_rows+1):
        start = i*x-x
        end = i*x
        layer.append(image[start:end])
        if i % y == 0:
            fin.append(layer)
            layer = []
    return fin

image_parsed = parse(image,25,6)

answer = [10000000, 0]
for layer in image_parsed:
    zero = 0
    one = 0
    two = 0
    for row in layer:
        zero += row.count('0')
        one += row.count('1')
        two += row.count('2')
    if zero < answer[0]:
        answer[0] = zero
        answer[1] = one * two
print('part1: {}'.format(answer[1]))

layer = ''
for y in range(6):
    for x in range(25):
        row = ''
        for l in range(100):
            if image_parsed[l][y][x] != '2':
                if image_parsed[l][y][x] == '1':
                    row += '#'
                else:
                    row += ' '
                break
        layer += row
print(layer)





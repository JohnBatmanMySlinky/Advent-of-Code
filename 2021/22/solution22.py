dat = []
with open("input.txt") as f:
    for line in f.readlines():
        line = line.replace("on", "1").\
            replace("off", "0").\
            replace("x", "").\
            replace("y", "").\
            replace("z", "").\
            replace("=", "").\
            replace("..", ",").\
            replace(" ", ",")

        # tuple of [status, (xmin, xmax, ymin, ymax, zmin, zmax)]
        newline = [int(x) for x in line.split(",")]
        titles = ["status", "xmin", "xmax", "ymin", "ymax", "zmin", "zmax"]

        dat.append(
            {x:y for x,y in zip(titles, newline)}
        )

def intersect(cube1, cube2):
    if cube1['xmax'] < cube2['xmin'] or cube1['xmin'] > cube2['xmax']:
        return None
    elif cube1['ymax'] < cube2['ymin'] or cube1['ymin'] > cube2['ymax']:
        return None
    elif cube1['zmax'] < cube2['zmin'] or cube1['zmin'] > cube2['zmax']:
        return None
    else:
        return {
            'xmin': max(cube1['xmin'], cube2['xmin']),
            'xmax': min(cube1['xmax'], cube2['xmax']),
            'ymin': max(cube1['ymin'], cube2['ymin']),
            'ymax': min(cube1['ymax'], cube2['ymax']),
            'zmin': max(cube1['zmin'], cube2['zmin']),
            'zmax': min(cube1['zmax'], cube2['zmax']),
        }

def difference(cube1, cube2):
    intersection = intersect(cube1, cube2)
    if intersection is None:
        return [cube1]
    
    differences = [
        {'xmin': cube1['xmin'], 'xmax':cube1['xmax'], 'ymin':cube1['ymin'], 'ymax':cube1['ymax'], 'zmin':cube1['zmin'],          'zmax':intersection['zmin']-1},
        {'xmin': cube1['xmin'], 'xmax':cube1['xmax'], 'ymin':cube1['ymin'], 'ymax':cube1['ymax'], 'zmin':intersection['zmax']+1, 'zmax':cube1['zmax']},

        {'xmin': cube1['xmin'],          'xmax':intersection['xmin']-1, 'ymin':cube1['ymin'], 'ymax':cube1['ymax'], 'zmin':intersection['zmin'], 'zmax':intersection['zmax']},
        {'xmin': intersection['xmax']+1, 'xmax':cube1['xmax'],          'ymin':cube1['ymin'], 'ymax':cube1['ymax'], 'zmin':intersection['zmin'], 'zmax':intersection['zmax']},

        {'xmin': intersection['xmin'], 'xmax':intersection['xmax'], 'ymin':cube1['ymin'],          'ymax':intersection['ymin']-1, 'zmin':intersection['zmin'], 'zmax':intersection['zmax']},
        {'xmin': intersection['xmin'], 'xmax':intersection['xmax'], 'ymin':intersection['ymax']+1, 'ymax':cube1['ymax'],          'zmin':intersection['zmin'], 'zmax':intersection['zmax']},
    ]

    return [x for x in differences if check_valid(x)]

def check_valid(cube):
    if (cube['xmin'] <= cube['xmax']) and (cube['ymin'] <= cube['ymax']) and (cube['zmin'] <= cube['zmax']):
        return True
    else:
        return False

def volume1(cube):
    xmax = min(50, cube['xmax'])
    xmin = max(-50, cube['xmin'])

    ymax = min(50, cube['ymax'])
    ymin = max(-50, cube['ymin'])

    zmax = min(50, cube['zmax'])
    zmin = max(-50, cube['zmin'])
    return max(xmax-xmin+1,0)*max(ymax-ymin+1,0)*max(zmax-zmin+1,0)

def volume2(cube):
    return (cube['xmax']-cube['xmin']+1)*(cube['ymax']-cube['ymin']+1)*(cube['zmax']-cube['zmin']+1)

universe = []
for instruction in dat:
    status = instruction.pop('status')
    new_universe = []

    # set difference handles off implicitly
    for cube in universe:
        new_universe += difference(cube, instruction)

    # for on, add em back 
    if status == 1:
        new_universe += [instruction]
    universe = new_universe.copy()

print(f"part 1 solution: {sum([volume1(x) for x in universe])}")
print(f"part 2 solution: {sum([volume2(x) for x in universe])}")





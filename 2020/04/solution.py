with open('input.txt','r') as f:
    dat = []
    passport = []
    for row in f.readlines():
        if row == '\n':
            dat.append(dict(zip(*[iter(passport)]*2)))
            passport = []
        else:
            passport += row.replace('\n','').replace(':',' ').split(' ')
    dat.append(dict(zip(*[iter(passport)]*2)))

def check_valid_keys(passport):
    return(sum([x in each.keys() for x in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']]) == 7)

def check_valid_values(passport):
    byr = (1920 <= int(passport['byr']) <= 2002) & (len(passport['byr']) == 4)
    iyr = (2010 <= int(passport['iyr']) <= 2020) & (len(passport['iyr']) == 4)
    eyr = (2020 <= int(passport['eyr']) <= 2030) & (len(passport['eyr']) == 4)

    if passport['hgt'][-2:] == 'in':
        hgt = 59 <= int(passport['hgt'][:-2]) <= 76
    elif passport['hgt'][-2:] == 'cm':
        hgt = 150 <= int(passport['hgt'][:-2]) <= 193
    else:
        hgt = False

    hcl_ok = [str(x) for x in range(10)] + list(map(chr, range(97, 103))) + ['#']
    hcl = (passport['hcl'][0] == '#') & all([x in hcl_ok for x in passport['hcl']])

    ecl_ok = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    ecl = passport['ecl'] in ecl_ok

    pid = len(passport['pid'])==9

    return(all([byr, iyr, eyr, hgt, hcl, ecl, pid]))


valid_passports1 = 0
valid_passports2 = 0
for each in dat:
    check1 = check_valid_keys(each)
    valid_passports1 += check1
    if check1:
        valid_passports2 += check_valid_values(each)
print(valid_passports1)
print(valid_passports2)

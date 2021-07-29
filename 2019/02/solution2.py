with open(r"input.txt","r") as f:
    dat = [x.split(",") for x in f.readlines()][0]
    dat = [int(x) for x in dat]
    
dat[1] = 12
dat[2] = 2
    
pos = 0
while True:
    op = dat[pos]
    a,b,c = dat[pos+1], dat[pos+2], dat[pos+3]
    
    if op == 1:
        dat[c] = dat[a] + dat[b]
        pos += 4
    elif op == 2:
        dat[c] = dat[a] * dat[b]
        pos += 4
    elif op == 99:
        print(dat[0])
        break
    else:
        assert 0 > 0 
    
        
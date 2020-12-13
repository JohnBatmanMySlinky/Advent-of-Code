# 7, 13, x, x, 59, x, 31, 19
# 0,  1, 2, 3,  4, 5,  6,  7

# N mod 7  == 7 - 0
# N mod 13 == 13 - 1
# N mod 59 == 59 - 4
# N mod 31 == 31 - 6
# N mod 19 == 19 - 7
import sys

dat = [x.strip('\n') for x in sys.stdin]
bus = [int(x) if x != 'x' else 'x' for x in dat[1].split(',')]
rem = [(y-x)*(x>0) for x,y in enumerate(bus) if y != 'x']
bus = [x for x in bus if x != 'x']

# today we learn about chinese remainder theorum!
# https://crypto.stanford.edu/pbc/notes/numbertheory/crt.html
import numpy as np

def modular_inverse(m, a):
    # shitty brute force
    m = m % a
    for x in range(1,a):
        if (m*x)%a == 1:
            return(x)
    return(1)

def chinese_remainder_theorum(m, a):
    M = np.prod(m)
    tot = 0
    for m_i, a_i in zip(m, a):
        b_i = M/m_i
        tot += a_i * b_i * modular_inverse(b_i, m_i)
    return(tot % M)

print('' + str(chinese_remainder_theorum(bus, rem)))

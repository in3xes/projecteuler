#!/usr/bin/env python
#

#Using non-deterministic algorithm
#Miller-Rabin test
#Algorithm is self explanatory

import random as r
from primes import primes

def modulo(a, b, c):
    x, y = 1, a
    while b > 0:
        if b%2 == 1:
            x = (x*y)%c
        y = (y*y)%c
        b /= 2
    return x%c

def mulmod(a, b, c):
    x, y = 1, a
    while b > 0:
        if b%2 == 1:
            x = (x + y)%c
        y = (y*2)%c
        b /= 2
    return x%c

def fermat(num, iterations):
    if num == 1:
        return False
    for x in range(0, iterations):
        rand = int(r.random() * (10**10))%(num-1) + 1
        if modulo(rand, num-1, num) != 1:
            return False
    return True

def miller(num, iterations):
    p = num
    if num < 2:
        return False
    s = num - 1
    while s%2 == 0:
        s /= 2

    for x in range(0, iterations):
        rand = int(r.random() * (10*10))%(num - 1) + 1
        tmp = s
        mod = modulo(rand, tmp, num)
        while tmp != p - 1 and mod != 1 and mod != p - 1:
            mod = mulmod(mod, tmp, num)
            tmp *= 2
        if mod != p - 1 and tmp%2 == 0:
            return False
    return True
    


if __name__ == '__main__':
    count = 0
    for x in range(1, 10 ** 6):
        if miller(x, 10):
            if x not in primes:
                count += 1
                print 'Boha, falied', x
    print count

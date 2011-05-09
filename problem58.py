#!/usr/bin/env python
#


from primes import primes
from math import sqrt
from isprimes import fermat

def corners(num):
    l = 2*num - 1
    s = (l - 2) ** 2 + 1
    c1 = s + l - 2
    c2 = c1 + l - 1
    c3 = c2 + l - 1
    c4 = c3 + l - 1
    return [c1, c2, c3, c4]

def nps(l):
    count = 0
    for x in l:
        if fermat(x, 20):
            count += 1
    return count

if __name__ == '__main__':
    totalprimes = 0
    totalnum = 1
    n = 2
    while True:
        c = corners(n)
        totalprimes += nps(c)
        totalnum = (n-1) * 4 + 1
        pc = (totalprimes * 100)/totalnum 
        if pc < 10:
            break
        n += 1

    print n

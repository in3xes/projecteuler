#!/usr/bin/env python

from primes import primes
from tmp import p

primes += p

def primefact(num):
    count = 0
    pfact = []
    p = 0
    while True:
        if count >= 40:
            break
        pr = primes[p]
        if pr/2 > num:
            break
        elif num%pr == 0:
            pfact.append(pr)
            num = num/pr
            count += 1
            print count, p, pr
            p = 0


        else:
            p += 1

    return sum(pfact)


if __name__ == '__main__':
    num = ''
    for x in xrange(1, 100):
        num = num + '1'

    num = int(num)
    print primefact(num)
    

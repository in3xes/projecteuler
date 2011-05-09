#!/usr/bin/env python
#

from primes import primes

n = 21000
while True:
    p = primes[n - 1]
    if n % 2 == 0:
        n += 1
        continue
    s = (p - 1) ** n + (p + 1) ** n
    rem = s % (p ** 2)
    print n, p, rem
    if rem > 10 ** 10:
        print p, n
        break
    n += 1

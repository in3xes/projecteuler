#!/user/bin/env python

#better algo to find primality of a number
#devide by all the primes less then sqrt(N)

import math as m
from primes import primes

prime = primes[:]
n = 1299691
while n < 10 ** 10:
    p = True
    sq = m.sqrt(n)
    for x in primes:
        if x > sq:
            break
        if n % x == 0:
            p = False
            break
    if p:
	f = open('pr', 'a')
	f.write(str(n)+',')
	f.close()
	prime.append(n)
    n += 2



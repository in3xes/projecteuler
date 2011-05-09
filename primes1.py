#!/usr/bin/env python

#
#Delete all the multiples of primes

def genprimes(max):
    primes = [x for x in xrange(3, max + 1, 2)]
    primes = set(primes)
    for a in (3, 5, 7, 11, 13, 17, 19):
        print a
        b = set([x for x in xrange(a, max+1, a)])
        primes = primes - b
        del b

    primes = list(primes)
    primes.sort()

    for n in primes:
        print n
        tmp = n * 2
        while tmp < max:
            try:
                primes.remove(tmp)
                tmp = tmp + n
            except:
                tmp = tmp + n
                pass

    return primes

if __name__ == '__main__':
    p = genprimes(1000000000)
    charp = [str(x) for x in p]
    f = open('pr', 'w')
    f.write(','.join(charp))
    f.close()

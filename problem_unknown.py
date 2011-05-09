#!/usr/bin/env python

#All the 1-9 palindrome are divisible by 3. Should check for 1-n
#where n < 9
#
#use recursive algorithm to generate all the permutation


from perm import perm
from primes import primes
import math as m


def num(l):
    l.reverse()
    number = 0
    for i, n in enumerate(l):
        number = number + n*(10**i)

    return number

def isprime(number):
    ans = True
    sqrt = m.sqrt(number)
    for p in primes:
        if p > sqrt:
            break
        if number%p == 0:
            ans = False
            break

    return ans


if __name__ == '__main__':
    a = []
    for x in range(1, 8):
        p = perm([n for n in range(1, x + 1)], lorg=[], recur_level=0, permutations=[])
        for n in p:
            number = num(n)
            if isprime(number):
                a.append(number)


    a.sort()
    print a

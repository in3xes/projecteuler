#!/usr/bin/env python

from primefactors import primefact
import operator

def prod(lst):
    pr = 1
    for x in lst:
        pr = pr*x

    return pr

def rad(n):
    prfact = primefact(n)
    return prod(prfact)

if __name__ == '__main__':
    rad_list = {}
    for x in range(1, 100001):
        print x
        rad_list[x] = rad(x)

    d = rad_list
    d = sorted(d.iteritems(), key=operator.itemgetter(1))
    print d[9999]

#!/usr/bin/env python
#
#

##Normal bruteforce checing

from primes import primes
from perm import perm

def inti(lst):
    lst.reverse()
    ans = 0
    for i, x in enumerate(lst):
        ans += x * 10**i
    return ans

def rotate(num):
    s = str(num)
    slist = [int(x) for x in s]
    slist = perm(slist, [], 0, [])
    slist = [inti(x) for x in slist]
    ans = []
    for x in slist:
        if x in primes:
            ans.append(x)
    ans.sort()
    return ans

def sol(num):
    lst = list(rotate(num))
    for x in range(0, len(lst) - 2):
        a = lst[x]
        for y in range(x, len(lst) - 1):
            b = lst[y]
            for z in range(y, len(lst)):
                c = lst[z]
                if a != b and b!= c:
                    if c - b == b - a:
                        print a, b, c
                        break

            

if __name__ == '__main__':
    for x in primes:
        if len(str(x)) == 4:
            print x
            num = x
            sol(num)
    

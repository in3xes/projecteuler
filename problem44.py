#!/usr/bin/env python
#

import math as m
def perfsq(num):
    a = m.sqrt(num)
    if int(a) == a:
        return True
    return False

def ispent(num):
    ans = False
    det = 1 + 24 * num
    if perfsq(det):
        sq = m.sqrt(det)
        if (sq + 1) % 6 == 0:
            ans = True

    return ans


if __name__ == '__main__':
    pent = []
    n = 1
    a = None
    p = lambda n: (n*(3*n - 1))/2
    while True:
        curr = p(n)
        pent.append(curr)
        for x in pent:
            if ispent(curr + x):
                print curr, x, curr+x
                if curr-x in pent:
                    print "Ans:", curr, x, curr - x, curr + x
                                        

        n += 1

#!/usr/bin/env python
#

import math as m

def nxt(num):
    ans = 0
    for x in str(num):
        ans += m.factorial(int(x))

    return ans

def chainlen(num):
    chain = []
    while True:
        chain.append(num)
        num = nxt(num)
        if num in chain:
            return len(chain)


if __name__ == '__main__':
    count = 0
    for x in range(1, 10 ** 6):
        l = chainlen(x)
        print x, l, count
        if l == 60:
            count += 1



    print count

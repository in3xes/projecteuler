#!/usr/bin/env python
#

#No logic required
#

def sumsq(num):
    ans = 0
    for x in str(num):
        tmp = int(x)
        ans += tmp ** 2

    return ans

def sol(num):
    a = num
    while True:
        a = sumsq(a)
        if a == 1 or a == 89:
            break

    return a


if __name__ == '__main__':
    count = 0
    for x in range(2, 10000000):
        a = sol(x)
        print x, a
        if a == 89:
            count += 1


    print count

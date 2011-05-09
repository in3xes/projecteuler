#!/usr/bin/env python
#

def isans(num):
    for x in str(num):
        if int(x) > 2:
            return False

    return True

def multi(num):
    n = 1
    while True:
        if isans(num * n):
            break
        n += 1

    return n
def lst(num):
    a = []
    for x in str(num):
        a.append(int(x))
    a.reverse()
    return a

def num(lst):
    a = 0
    for i, x in enumerate(lst):
        a += x * 10 ** i

    return a

def incr(tri):
    pos = 0
    while True:
        if pos < len(tri):
            buff = tri[pos]
            buff += 1
            if buff < 3:
                tri[pos] = buff
                return tri
            tri[pos] = 0
            pos += 1
        else:
            tri.insert(len(tri), 1)
            return tri

        

if __name__ == '__main__':
    # ans = 0
    # n = 0
    # for x in range(1, 10000):
    #     n = multi(x)
    #     print x, n, x*n
    #     ans += n

    # print ans

    ans = 0
    for x in range(1, 10000):
        print x
        n = 1
        while True:
            if n % x == 0:
                ans += n/x
                break
            else:
                n = num(incr(lst(n)))


    print ans + 1

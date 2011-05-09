#!/usr/bin/env python
#
#check each number weather a bouncy
#number of not.
#
#This is basically brute force.
#
#


def bouncy(num):
    l, g = False, False
    s = str(num)
    for x in range(0, len(s) - 1):
        n = int(s[x])
        m = int(s[x+1])
        if n > m:
            l = True

        if n < m:
            g = True

        if l and g:
            return True

    return False


if __name__ == '__main__':
    n = 100
    b = 0
    while True:
        if bouncy(n):
            b += 1
            p = float((b*100))/float(n)
            print n, p
            if p >= 99:
                print 'Ans: ', n
                break

        n += 1

#!/usr/bin/env python
#

import math as m


def isans(num):
    num = str(num)
    print num, len(num)
    for x in range(1, 9):
        if int(num[2*x - 2]) == x:
            pass
        else:
            return False
    return True



if __name__ == '__main__':
    a = 101010101
    b = 138902663
    s = 10101010
    n = s * 10 + 3
    while  True:
        if isans(n ** 2):
            print n
            break
        n = s * 10 + 7
        if isans(n ** 2):
            print n
            break
        s += 1
        n = s* 10 + 3

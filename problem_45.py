#!/usr/bin/env python
# Failed

import math

def solvable(a, b, c):
    if perfroot(disc(a, b, c)):
        # tst = math.sqrt(disc(a, b, c))/ (2 * a)
        # print tst
        # if int(tst) == tst:
        return True
    return False


def disc(a, b, c):
    return b ** 2 - 4 * a * c

def perfroot(n):
    try:
        root = math.sqrt(n)
    except:
        return False
    proot = int(root)
    if proot == root:
        return True
    return False
    
def test(a, b, c):
    if solvable(a, b, c):
        print 'Solvable'
        return True
    else:
        print 'Not solvable'
        return False

value = lambda n: n * (n + 1)

def p(idx):
    lst = [3, -1]
    lst.append(-value(idx))
    return lst


def h(idx):
    lst = [4, -2]
    lst.append(-value(idx))
    return lst

def solve(a, b, c):
    return -b + (math.sqrt( b ** 2 - 4 * a * c))/(2 * a), -b - (math.sqrt( b ** 2 - 4 * a * c))/(2 * a)



if __name__ == '__main__':
    # test(1, 2, 1)
    # test(1, 2, 3)
    # a = p(2)
    # print a
    x = 288
    while True:
        a = h(x)
        if solvable(a[0], a[1], a[2]):
            b = p(x)
            if solvable(b[0], b[1], b[2]):
                print x
                ans = solve(a[0], a[1], a[2])
                print ans
                ans = solve(b[0], b[1], b[2])
                print ans
#                break
        x = x + 1

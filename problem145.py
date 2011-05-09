#!/usr/bin/env python
#

def isans(num):
    odds = [1, 3, 5, 7, 9]
    a = str(num)
    if int(a[-1]) == 0:
        return False
    b = a[::-1]
    c = num + int(b)
    c = str(c)
    for x in c:
        if int(x) in odds:
            pass
        else:
            return False

    return True


if __name__ == '__main__':
    count = 0
    for n in xrange(1, 10 ** 9):
        if isans(n):
            print n, count
            count += 1

    print count
        

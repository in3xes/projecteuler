#!/usr/bin/env python

#
#


def ispan(num):
    if len(str(num)) != 9:
        return False
    check = [n for n in range(1, 10)]
    for x in str(num):
        if int(x) in check:
            check.remove(int(x))
        else:
            return False

    return True

def givespan(num):
    n = 1
    ans = ''
    while len(ans) <=9:
        ans = ans+str(num * n)
        if ispan(ans):
            return int(ans)
        n += 1

    return None
        


if __name__ == '__main__':
    # if ispan(192837465):
    #     print 'working'
    # else:
    #     print 'not working'

    for x in range(1, 10000):
        ans = givespan(x)
        if ans is not None:
            print ans, x
            

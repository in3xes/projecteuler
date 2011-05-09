#!/usr/bin/env python
#No logic

#
#


def ispalin(st):
    if st == st[::-1]:
        return True
    return False

if __name__ == '__main__':
    start = 1
    ans = 0
    palins = []
    while start < 10 ** 4:
        pos = start
        total = 0
        chain = []
        while total < 10 ** 8:
            if ispalin(str(total)):
                if len(chain) >= 2:
                    if total not in palins:
                        ans = ans + total
                        palins.append(total)
                    print total, start
            total += pos **2
            chain.append(pos)
            pos += 1
        start += 1

    print ans

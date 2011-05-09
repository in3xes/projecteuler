#!/usr/bin/env python


def brake(num):
    string = str(num)
    return sorted([int(x) for x in string])


def check(num):
    l1 = brake(num)
    l2 = brake(num * 2)
    if l1 == l2:
        l3 = brake(num * 3)
        if l2 == l3:
            l4 = brake(num * 4)
            if l3 == l4:
                l5 = brake(num * 5)
                if l4 == l5:
                    l6 = brake(num * 6)
                    if l5 == l6:
                        for x in range(1, 7):
                            print num * x
                        return True

    return False


n = 0
ans = 0
while True:
    start = 10 ** n
    end = (10 ** (n + 1)) / 6 + 1
    chk = False
    for num in range(start, end):
        if check(num):
            chk = True
            ans = num
            break

    if chk:
        break
    n = n + 1


print ans

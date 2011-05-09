#!/usr/bin/env python

#Problem ## 53

#
#No logic, Bruteforce

def f(num):
    if num == 0:
        return 1
    f = 1
    for x in range(1, num + 1):
        f = f * x
    return f

def ncr(n, r):
    if n < r:
        return None
    return f(n)/(f(n - r) * f(r))

limit = 10 ** 6
ans = 0
for x in range(1, 101):
    for y in range(1, x+1):
        if ncr(x, y) > limit:
            ans += 1


print ans

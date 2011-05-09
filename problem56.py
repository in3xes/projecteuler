#!/usr/bin/env python

#Problem ## 59

#
#No logic, Bruteforce

def sumofdig(num):
    s = 0
    for n in str(num):
        s += int(n)

    return s

ans = 0
for a in range(1, 100):
    for b in range(1, 100):
        s = sumofdig(a ** b)
        if s > ans:
            ans = s
            print ans, a, b

print ans

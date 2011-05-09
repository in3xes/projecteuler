#!/usr/bin/env python

#Problem ## 97

#
#To find lat 10 digits we should only care about last 11 digits
#To be safe consider 13 digits


def l(num):
    return int(str(a)[-13:])

a = 2 ** 100
for x in range(101, 7830458):
    a = l(a)
    a = a * 2
    if x%10000 == 0:
        print a, x

a = a * 28433
a = a +1

print a




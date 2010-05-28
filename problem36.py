#!/usr/bin/python

def reverse(val):
    rev = ""
    for x in str(val):
        rev = x + rev
    return int(rev)

def bina(val):
    bin = ""
    while(val>=2):
        bin = str(val%2) + bin
        val = val/2
    bin = str(val) + bin
    return int(bin)

def ispolin(val):
    if val == reverse(val):
        return True

count = 0
total = 0
for x in range(1, 1000000):
    if ispolin(x) and ispolin(bina(x)):
        print x, bina(x)
        count = count + 1
        total = total + x

print count, total

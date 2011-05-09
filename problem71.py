#!/usr/bin/env python

#Find the largest number less than 3/7 with
#the given number as numerator and check the 
#nearest co-prime with numerator and value
#less than 3/7

#Logic: Mutliply with 3 and devide with 7
#find the nearest co-prime with 


def coprime(a, b):
    if b < a:
        a = a + b
        b = a - b
        a = a - b
    if b%a == 0:
        return False
    while(True):
        tmp = b%a
        b = a
        a = tmp
        if a == 1:
            return True
        elif a == 0:
            return False
        else:
            continue

def nextcoprime(a, b):
    ans = False
    while(!ans):
        b = b + 1
        if coprime(a, b):
def ans():
    for n in xrange(4, 1000000):
        a = float(3)/float(7)
        ans = a
        num = (n*3)/7

if __name__ == "__main__":
    print coprime(42, 63)


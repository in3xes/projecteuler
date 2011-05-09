#!/usr/bin/env python
#
#

#Normal bruteforce check

count = 0
a = 0
n = 0
while True:
    x = 1
    a = x ** n
    while len(str(a)) <= n:
        if len(str(a)) == n:
            count += 1
            print a, n, count

        x += 1
        a = x ** n

    n += 1

    
    
        
    

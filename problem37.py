#!/usr/bin/env python
#problem 37 from projecteuler.net
#this is solved by loading all the primes below 10 ** 6
#a text file

import pn
ans = []
for x in pn.a:
    x = str(x)
    for y in range(1, len(x)+1):
        tmp = x[:y]
        if int(tmp) in pn.a:
            if y == len(x):
                for z in range(0, len(x)):
                    tmpr = x[z:]
                    if int(tmpr) in pn.a:
                        if z == len(x)-1:
                            ans.append(int(x))
                            print ans
                    else:
                        break
        else:
            break

print ans
            


        
